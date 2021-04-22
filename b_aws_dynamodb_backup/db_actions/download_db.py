import json
from typing import Any, Dict, List, Optional
from pathlib import Path

from b_aws_dynamodb_backup.color_print import cprint
from b_aws_dynamodb_backup.db_actions.base_db_action import BaseDbAction
from b_aws_dynamodb_backup.print_colors import PrintColors


class DownloadDb(BaseDbAction):
    def __init__(self):
        super().__init__()

    def download(self, table_name: str, download_dir: Optional[str] = None) -> None:
        """
        Downloads a whole dynamodb table to a specified download dir.
        """

        # Ensure that the download directory is available.
        download_dir = download_dir or self.default_directory(table_name)
        Path(download_dir).mkdir(parents=True, exist_ok=True)

        continuation_key = None
        iteration = 1

        cprint(PrintColors.OKBLUE, f'Downloading {table_name} table...')

        while True:
            kwargs = dict(TableName=table_name)
            if continuation_key:
                kwargs['ExclusiveStartKey'] = continuation_key

            try:
                response: Dict[Any, Any] = self.client.scan(**kwargs)
            except self.client.exceptions.ResourceNotFoundException:
                cprint(PrintColors.FAIL, 'Table not found!')
                return

            items: List[Dict[Any, Any]] = response['Items']
            count: int = response['Count']
            continuation_key = response.get('LastEvaluatedKey')

            if count == 0:
                break

            with open(f'{download_dir}/{self.create_backup_file_name(iteration)}', 'a') as file:
                file.write(json.dumps(items))

            cprint(PrintColors.OKGREEN, f'Successfully created chunk {iteration} with {count} database items.')

            if not continuation_key:
                break

        cprint(PrintColors.OKGREEN, 'Successfully finished download operation.')

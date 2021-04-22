import json
from typing import Optional
from os import listdir
from os.path import isfile, join

from b_aws_dynamodb_backup.color_print import cprint
from b_aws_dynamodb_backup.db_actions.base_db_action import BaseDbAction
from b_aws_dynamodb_backup.print_colors import PrintColors


class UploadDb(BaseDbAction):
    def __init__(self):
        super().__init__()

    def upload(self, table_name: str, backups_dir: Optional[str] = None) -> None:
        backups_dir = backups_dir or self.default_directory(table_name)

        full_paths = [join(backups_dir, f) for f in listdir(backups_dir) if self.is_backup_file(f)]
        file_paths = [f for f in full_paths if isfile(f)]

        if len(file_paths) < 1:
            cprint(PrintColors.FAIL, f'Directory ({backups_dir}) does not contain any backup files!')

        for file in file_paths:
            with open(file, 'r') as data_file:
                data = data_file.read()
                data = json.loads(data)

                put_items = [self.create_put_item(item) for item in data]

                for chunk in self.batch_put_items(put_items):
                    self.client.batch_write_item(
                        RequestItems={
                            table_name: chunk
                        }
                    )

                    cprint(
                        PrintColors.OKGREEN,
                        f'Successfully uploaded restore data to the table with {len(chunk)} items.'
                    )

                cprint(PrintColors.OKGREEN, 'Successfully restored the table.')

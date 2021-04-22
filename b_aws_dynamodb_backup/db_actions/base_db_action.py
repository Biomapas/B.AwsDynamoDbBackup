from typing import List, Any, Iterator, Dict

import boto3


class BaseDbAction:
    def __init__(self):
        self.client = boto3.client('dynamodb')

    @classmethod
    def create_backup_file_name(cls, iteration: int) -> str:
        return f'backup-chunk{iteration}.json'

    @classmethod
    def is_backup_file(cls, file_name: str) -> bool:
        return file_name.startswith('backup-chunk') and file_name.endswith('.json')

    @classmethod
    def default_directory(cls, table_name: str) -> str:
        return f'./{table_name}'

    @classmethod
    def batch_put_items(cls, items: List[Any]) -> Iterator[Any]:
        """
        Batches long list into smaller chunks for dynamodb put operations.
        """
        length = len(items)

        # Map Entries: Maximum number of 25 items.
        # Read more:
        # https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html
        n = 25

        for ndx in range(0, length, n):
            yield items[ndx:min(ndx + n, length)]

    @classmethod
    def create_put_item(cls, item: Dict[Any, Any]) -> Dict[Any, Any]:
        return {
            'PutRequest': {
                'Item': item
            }
        }

from typing import Any, Dict, List, Iterator
import string
import random

from b_aws_dynamodb_backup.color_print import cprint
from b_aws_dynamodb_backup.db_actions.base_db_action import BaseDbAction
from b_aws_dynamodb_backup.print_colors import PrintColors


class SeedDb(BaseDbAction):
    def __init__(self):
        super().__init__()

    def seed(self, table_name: str, data_count: int) -> None:
        cprint(PrintColors.OKBLUE, f'Seeding {table_name} table with {data_count} items...')

        response = self.client.describe_table(
            TableName=table_name
        )

        attributes = response['Table']['AttributeDefinitions']

        items = []
        for _ in range(data_count):
            items.append(self.random_item(attributes))

        put_items = []
        for item in items:
            put_items.append(self.create_put_item(item))

        for chunk in self.batch_put_items(put_items):
            self.client.batch_write_item(
                RequestItems={
                    table_name: chunk
                }
            )

            cprint(PrintColors.OKGREEN, f'Successfully seeded the table with {len(chunk)} items.')

        cprint(PrintColors.OKGREEN, 'Successfully seeded the table.')

    @classmethod
    def random_string(cls) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))

    @classmethod
    def random_item(cls, dynamodb_attributes: List[Dict[Any, Any]]) -> Dict[Any, Any]:
        item = {}

        for attribute in dynamodb_attributes:
            attr_name = attribute['AttributeName']
            attr_type = attribute['AttributeType']
            item[attr_name] = {attr_type: cls.random_string()}

        return item



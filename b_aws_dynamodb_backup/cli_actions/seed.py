import sys

from b_aws_dynamodb_backup.db_actions.seed_db import SeedDb


def main():
    try:
        table_name = sys.argv[1]
    except IndexError:
        table_name = None

    SeedDb().seed(table_name, 500)

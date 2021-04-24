import sys

from b_aws_dynamodb_backup.db_actions.seed_db import SeedDb


def main():
    table_name = sys.argv[1]
    SeedDb().seed(table_name, 500)

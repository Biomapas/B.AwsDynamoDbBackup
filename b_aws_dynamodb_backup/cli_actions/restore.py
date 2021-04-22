import sys

from b_aws_dynamodb_backup.db_actions.upload_db import UploadDb


def main():
    try:
        table_name = sys.argv[1]
    except IndexError:
        table_name = None

    UploadDb().upload(table_name)

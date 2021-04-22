import sys

from b_aws_dynamodb_backup.db_actions.download_db import DownloadDb


def main():
    try:
        table_name = sys.argv[1]
    except IndexError:
        table_name = None

    DownloadDb().download(table_name)

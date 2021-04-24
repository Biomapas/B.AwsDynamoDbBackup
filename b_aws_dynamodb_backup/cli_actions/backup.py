import sys
from b_aws_dynamodb_backup.exceptions.database_not_found import DatabaseNotFound
from b_aws_dynamodb_backup.color_print import cprint
from b_aws_dynamodb_backup.cli_actions.base_cli_actions import get_all_tables, ask_y_n_question
from b_aws_dynamodb_backup.db_actions.download_db import DownloadDb
from b_aws_dynamodb_backup.print_colors import PrintColors


def main():
    try:
        table_names = [sys.argv[1]]
    except IndexError:
        table_names = get_all_tables()
        table_names_readable = '\n'.join(table_names)
        question = f'Are you sure you want to backup all these tables?:\n{table_names_readable}\n[y/n]: '

        if not ask_y_n_question(question):
            return

    for table_name in table_names:
        try:
            DownloadDb().download(table_name)
        except DatabaseNotFound as ex:
            cprint(PrintColors.FAIL, repr(ex))

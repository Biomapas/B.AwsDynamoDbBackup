from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

with open('VERSION') as file:
    VERSION = file.read()
    VERSION = ''.join(VERSION.split())

setup(
    name='b_aws_dynamodb_backup',
    version=VERSION,
    license='Apache License 2.0',
    packages=find_packages(exclude=['venv', 'b_aws_dynamodb_backup_test']),
    entry_points={
        'console_scripts': [
            'dyback=b_aws_dynamodb_backup.cli_actions.backup:main',
            'dyrest=b_aws_dynamodb_backup.cli_actions.restore:main',
            'dyseed=b_aws_dynamodb_backup.cli_actions.seed:main',
        ],
    },
    description=('DynamoDB.'),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'boto3',
        'b-continuous-subprocess>=0.3.2,<1.0.0',
    ],
    author='Laimonas Sutkus',
    author_email='laimonas.sutkus@biomapas.com',
    keywords='DynamoDB',
    url='https://github.com/biomapas/B.AwsDynamoDbBackup.git',
)

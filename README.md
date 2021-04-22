# B.AwsDynamoDbBackup

A python based package that allows you to back up, restore, and seed dynamodb database tables.

### Description

Sometimes you want to make a small modification to your dynamodb table, however it usually requires
destruction of the table itself. This library allows you to do those small modifications without 
any headache. You can easily backup all your data to your local computer, delete the table, create
a new one with desired modifications, and then simply restore it!

### Remarks

[Biomapas](https://biomapas.com) aims to modernise life-science 
industry by sharing its IT knowledge with other companies and 
the community. This is an open source library intended to be used 
by anyone. Improvements and pull requests are welcome.

### Related technology

- Python 3
- DynamoDB
- Boto3

### Assumptions

The project assumes the following:

- You have basic knowledge in python programming.
- You have basic knowledge in DynamoDB.

### Useful sources

- Read more DynamoDB:<br>
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKOverview.html

### Install

The project is built and uploaded to PyPi. Install it by using pip.

```
pip install b_aws_dynamodb_backup
```

Or directly install it through source.

```
pip install .
```

### Usage & Examples

The library exposes cli commands.

##### dyseed

Seeds your table with random data.

```shell
> dyseed TableName
```

##### dyback

Backups your whole table(s).

```shell
> dyback TableName
```

##### dyrest

Restores your whole table(s).

```shell
> dyrest TableName
```

### Testing

This project currently has no tests.

### Contribution

Found a bug? Want to add or suggest a new feature?<br>
Contributions of any kind are gladly welcome. You may contact us 
directly, create a pull-request or an issue in github platform.
Lets modernize the world together.

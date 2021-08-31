import base64
from typing import Any, Dict


class DynamoDbSerializer:
    @staticmethod
    def serialize_bytes(dynamodb_item: Dict[Any, Any]) -> None:
        """
        Finds bytes and converts them to base64 string.
        """
        for key, value in dynamodb_item.items():
            for inner_key, inner_value in value.items():
                # We found bytes field.
                if inner_key == 'B':
                    assert isinstance(inner_value, bytes)
                    value[inner_key] = base64.b64encode(value[inner_key]).decode('utf-8')

    @staticmethod
    def deserialize_bytes(dynamodb_item: Dict[Any, Any]) -> None:
        """
        Finds base64 string and converts to bytes.
        """
        for key, value in dynamodb_item.items():
            for inner_key, inner_value in value.items():
                # We found bytes field.
                if inner_key == 'B':
                    assert isinstance(inner_value, str)
                    value[inner_key] = base64.b64decode(value[inner_key])

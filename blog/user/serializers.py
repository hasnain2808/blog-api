from marshmallow import Schema, fields


class UserSerializer(Schema):
    name = fields.String(required=True, error_messages={"required": "Name required."})
    email = fields.Email(
        required=True, error_messages={"required": "Email ID required."}
    )

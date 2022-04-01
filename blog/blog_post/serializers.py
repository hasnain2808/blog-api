from marshmallow import Schema, fields


class BlogSerializer(Schema):
    user_id = fields.Integer(
        required=True, strict=True, error_messages={"required": "User id is required"}
    )
    title = fields.String(
        required=True, strict=True, error_messages={"required": "Title is required"}
    )
    content = fields.String(
        required=True, strict=True, error_messages={"required": "Content is required"}
    )

from mongoengine import Document, EmbeddedDocument, fields
import mongoengine
mongoengine.connect(
    db="tools",
    host="192.168.99.100"
)

class ToolInput(EmbeddedDocument):
    name = fields.StringField(required=True)
    value = fields.DynamicField(required=True)

class Tool(Document):
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    inputs = fields.ListField(fields.EmbeddedDocumentField(ToolInput))



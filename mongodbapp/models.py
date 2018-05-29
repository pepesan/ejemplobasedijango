from mongoengine import Document, EmbeddedDocument, fields
import mongoengine
mongoengine.connect(
    db="tools",
    host="localhost"
)

class ToolInput(EmbeddedDocument):
    name = fields.StringField(required=True)
    value = fields.DynamicField(required=True)

class Tool(Document):
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    inputs = fields.ListField(fields.EmbeddedDocumentField(ToolInput))



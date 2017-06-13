from flask_inputs.validators import JsonSchema
from flask_inputs import Inputs

schema = {
    'type': 'object',
    'properties': {
        'article_id': {
            'type': 'number',
            'required': True
        },
        'tag_names': {
            'type': 'array',
            'items': {
                'type': 'string'
            }
        },
    }
}

class AddValidator(Inputs):
    json = [JsonSchema(schema=schema)]

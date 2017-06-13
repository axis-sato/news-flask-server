add_schema = {
    "type": "object",
    "properties": {
        "article_id": {
            "type": "number",
        },
        "tag_names": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "additionalProperties": False,
    "required": ["article_id", "tag_names"]
}

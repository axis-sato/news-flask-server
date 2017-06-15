from functools import wraps
from jsonschema import Draft4Validator, ValidationError
from flask import jsonify, request, current_app


def _validate(schema, data):
    validator = Draft4Validator(schema)
    errors = [dict(
        message=e.message,
        params=[p for p in e.path],
        reason=e.validator,
        #schema=e.schema,
        #validator_value=e.validator_value
    ) for e in validator.iter_errors(data)]
    return errors

def validate_schema(schema):
    def wrapper(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            input = request.get_json(force=True)
            errors = _validate(schema, input)
            current_app.logger.debug(errors)
            if errors:
                response = jsonify(dict(success=False,
                                        message="invalid input",
                                        errors=errors))
                response.status_code = 422
                return response
            else:
                return fn(*args, **kwargs)
        return wrapped
    return wrapper

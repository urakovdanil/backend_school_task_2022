"""
Модуль содержит схемы для валидации данных в запросах и ответах.
Схемы валидации запросов используются в бою для валидации данных отправленных
клиентами.
Схемы валидации ответов *ResponseSchema используются только при тестировании,
чтобы убедиться, что обработчики возвращают данные в корректном формате.
"""
from marshmallow import Schema, ValidationError, validates, validates_schema
from marshmallow.fields import Date, DateTime, AwareDateTime, Dict, Float, Int, List, Nested, Str
from marshmallow.validate import Length, OneOf, Range

from pytz import utc


BIRTH_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'


class ElementSchema(Schema):
    id = Str(validate=Length(min=1, max=255), strict=True, required=True, allow_none=False)
    url = Str(validate=Length(min=1, max=255), required=False, allow_none=True)
    parentId = Str(validate=Length(min=1, max=255), required=True, allow_none=True)
    size = Int(validate=Range(min=1), allow_none=True)
    type = Str(validate=OneOf(['FILE', 'FOLDER']))


class ImportSchema(Schema):
    items = List(Nested(ElementSchema), many=True, required=True,
                      validate=Length(max=10000))
    updateDate = AwareDateTime(format='iso8601', default_timezone=utc, required=True, allow_none=False)

    @validates_schema
    def validate_unique_citizen_id(self, data, **_):
        item_ids = set()
        for item in data['items']:
            if item['id'] in item_ids:
                raise ValidationError(
                    'id %r is not unique' % item['id']
                )

            item_ids.add(item['id'])
            if item['type'] == 'FOLDER':
                if 'size' in item.keys() and item['size'] is not None:
                    raise ValidationError('size of any folder (%r) cannot be declared on import' % item['id'])
                if 'url' in item.keys() and item['url'] is not None:
                    raise ValidationError('url of any folder (%r) cannot be declared' % item['id'])
            elif item['type'] == 'FILE':
                if 'url' not in item.keys():
                    raise ValidationError('url of any file (%r) must be declared' % item['id'])
                elif item['url'] is None:
                    raise ValidationError('url of any file (%r) must be declared' % item['id'])
                if 'size' not in item.keys():
                    raise ValidationError('size of any file (%r) must be declared' % item['id'])


class ImportIdSchema(Schema):
    import_id = Int(strict=True, required=True)

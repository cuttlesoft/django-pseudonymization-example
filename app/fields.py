from django.db.models.fields import Field


class PseudonymizedField(Field):
    def __init__(self, field_type=None, methods=(None, None), *args, **kwargs):
        self.field_type = field_type
        self.mask, self.unmask = methods

        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.field_type is not None:
            kwargs['field_type'] = self.field_type
        if self.mask is not None and self.unmask is not None:
            kwargs['methods'] = (self.mask, self.unmask)
        return name, path, args, kwargs

    def get_internal_type(self):
        return self.field_type().get_internal_type()

    def get_prep_value(self, value):
        return super().get_prep_value(self.mask(value))

    def from_db_value(self, value, expression, connection, context):
        return self.unmask(value)

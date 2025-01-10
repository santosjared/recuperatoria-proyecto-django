import re
from django.core.exceptions import ValidationError

def validate_alphabet(value):
    if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', value):
        raise ValidationError('Este campo solo puede contener letras.')
def validate_no_negative(value):
    if value<0:
        raise ValidationError('El valor no debe ser negativo')
def validate_price_limit(value):
    if value >100000:
        raise ValidationError('El precio no debe ser mayor a 100000')
def validate_stock_limit(value):
    if value > 10000:
        raise ValidationError('El stock no debe ser mayor a 10000')
def validate_international_phone_number(value):
    if not re.match(r'^\+\d{1,3}\s?\d{4,14}$', value):
        raise ValidationError('El número telefónico debe incluir el código de país (por ejemplo, +591 para Bolivia).')

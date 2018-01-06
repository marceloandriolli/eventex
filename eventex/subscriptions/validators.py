from django.core.exceptions import ValidationError


def validate_cpf(value):
    """Validate CPF as a digits and lenght eleven """
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 numeros.', 'length')

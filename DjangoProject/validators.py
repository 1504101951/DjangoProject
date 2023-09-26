from django.core.exceptions import ValidationError
import re


def validate_password_complexity(password):
    if len(password) < 8:
        raise ValidationError("密码长度至少为8个字符")
    if not any(char.isdigit() for char in password):
        raise ValidationError("密码必须包含至少一个数字")
    if not any(char.isalpha() for char in password):
        raise ValidationError("密码必须包含至少一个字母")
    if not any(char.isupper() for char in password):
        raise ValidationError("密码必须包含至少一个大写字母")
    if not any(char.islower() for char in password):
        raise ValidationError("密码必须包含至少一个小写字母")


def validate_phone_number(phone):
    if not phone.isdigit() or len(phone) != 11:
        raise ValidationError("请输入正确的手机号")


def validate_email(email):
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        raise ValidationError("请输入正确的邮箱地址")

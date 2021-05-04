from django.core.validators import RegexValidator

name_regex = RegexValidator(
    regex=r"[A-Za-z]+$",
    message="Name must consist of letters only. Up to 50 letters allowed.",
)

phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
)

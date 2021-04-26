from rest_framework.exceptions import APIException


class AlreadyEdited(APIException):
    status_code = 400
    default_detail = "Vignette start date was already edited once."
    default_code = "already_edited"


class AfterStartDate(APIException):
    status_code = 400
    default_detail = "Validity of vignette already started."
    default_code = "already_started"


class MaxDaysExceeded(APIException):
    status_code = 400
    default_detail = "Vignette cannot be delayed for more thank 90 days from start day."
    default_code = "max_days_exceeded"

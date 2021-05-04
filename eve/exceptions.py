# -*- coding: utf-8 -*-

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


class UserCheckFailed(APIException):
    status_code = 403
    default_detail = "Access forbidden. The client may be unauthorized or trying to access data that " \
                     "does not belong to him. "
    default_code = "access_denied"

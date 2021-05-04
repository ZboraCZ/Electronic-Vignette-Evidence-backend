# -*- coding: UTF-8 -*-

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ValidatedVignette:
    valid: bool
    status: str
    valid_from: datetime
    expire_date: datetime

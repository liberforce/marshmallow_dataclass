from dataclasses import field
import datetime
from typing import (ClassVar, Type)

import marshmallow

from marshmallow_dataclass import dataclass


@dataclass
class User:
    birth: datetime.date = field(metadata={
        "required": True  # A parameter to pass to marshmallow's field
    })
    website: str = field(metadata={
        "marshmallow_field": marshmallow.fields.Url()  # Custom marshmallow field
    })
    Schema: ClassVar[Type[marshmallow.Schema]] = marshmallow.Schema  # For the type checker

from typing import (ClassVar, Type)
import dataclasses
import marshmallow
from marshmallow_dataclass import (NewType, dataclass)

Email = NewType('Email', str, field=marshmallow.fields.Email)


@dataclass
class ContactInfo:
    mail: Email = dataclasses.field(default="anonymous@example.org")
    Schema: ClassVar[Type[marshmallow.Schema]] = marshmallow.Schema


ContactInfo.Schema().load({})
ContactInfo(mail='anonymous@example.org')

ContactInfo.Schema().load({"mail": "grumble grumble"})

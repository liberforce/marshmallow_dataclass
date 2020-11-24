from typing import (ClassVar, Type)
import dataclasses
import marshmallow
from marshmallow_dataclass import (NewType, dataclass)

Email = NewType('Email', str, field=marshmallow.fields.Email)
Url = NewType('Url', str, field=marshmallow.fields.Url)


@dataclass
class ContactInfo:
    mail: Email = dataclasses.field(default="anonymous@example.org")
    url: Url = dataclasses.field(default='http://www.example.org')
    Schema: ClassVar[Type[marshmallow.Schema]] = marshmallow.Schema


# OK
ContactInfo.Schema().load({})

# OK
ContactInfo(
    mail='anonymous@example.org',
    url='http://anonymous.example.org',
)

# Malformed URL
ContactInfo.Schema().load({"url": "file:///toto.avi"})

# Malformed email
ContactInfo.Schema().load({"mail": "grumble grumble"})

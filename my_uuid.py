from typing import (ClassVar, Type)
import dataclasses
import uuid
import marshmallow
from marshmallow_dataclass import (NewType, dataclass)

Email = NewType('Email', str, field=marshmallow.fields.Email)
Url = NewType('Url', str, field=marshmallow.fields.Url)
UUID = NewType('UUID', uuid.UUID, field=marshmallow.fields.UUID)


@dataclass
class ContactInfo:
    mail: Email = dataclasses.field(default="anonymous@example.org")
    url: Url = dataclasses.field(default='http://www.example.org')
    id: UUID = dataclasses.field(default=uuid.uuid4())
    Schema: ClassVar[Type[marshmallow.Schema]] = marshmallow.Schema



# OK
ContactInfo.Schema().load({})

# OK
ContactInfo(
    mail='anonymous@example.org',
    url='http://anonymous.example.org',
    id=uuid.UUID('cb3411a6-a070-427c-8207-a8e4a7f7cb39'),
)

# OK
ContactInfo.Schema().load({"id": "cb3411a6-a070-427c-8207-a8e4a7f7cb39"})

# Malformed UUID
ContactInfo.Schema().load({"id": "blah"})

# Malformed URL
ContactInfo.Schema().load({"url": "file:///toto.avi"})

# Malformed email
ContactInfo.Schema().load({"mail": "grumble grumble"})

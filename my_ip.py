from typing import (ClassVar, Type)
import ipaddress
import dataclasses
import uuid
import marshmallow
from marshmallow_dataclass import (NewType, dataclass)

Email = NewType('Email', str, field=marshmallow.fields.Email)
Url = NewType('Url', str, field=marshmallow.fields.Url)
UUID = NewType('UUID', uuid.UUID, field=marshmallow.fields.UUID)
IPv4 = NewType('IPv4', ipaddress.IPv4Address, field=marshmallow.fields.IPv4)

@dataclass
class ContactInfo:
    email: Email = dataclasses.field(default="anonymous@example.org")
    url: Url = dataclasses.field(default='http://www.example.org')
    id: UUID = dataclasses.field(default=uuid.uuid4())
    ipv4: IPv4 = dataclasses.field(default=ipaddress.IPv4Address('127.0.0.1'))
    Schema: ClassVar[Type[marshmallow.Schema]] = marshmallow.Schema



# OK
ContactInfo(
    email='anonymous@example.org',
    url='http://anonymous.example.org',
    id=uuid.UUID('cb3411a6-a070-427c-8207-a8e4a7f7cb39'),
    ipv4=ipaddress.IPv4Address('192.168.0.1'),
)

# OK
ContactInfo.Schema().load({})

# OK
ContactInfo.Schema().load({"ipv4": "192.168.0.2"})

# OK
ContactInfo.Schema().load({"id": "cb3411a6-a070-427c-8207-a8e4a7f7cb39"})

# Malformed IPv4
ContactInfo.Schema().load({"ipv4": "192.168.0.256"})

# Malformed UUID
ContactInfo.Schema().load({"id": "blah"})

# Malformed URL
ContactInfo.Schema().load({"url": "file:///toto.avi"})

# Malformed email
ContactInfo.Schema().load({"email": "grumble grumble"})

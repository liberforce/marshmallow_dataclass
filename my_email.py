from dataclasses import dataclass, field
import marshmallow
import marshmallow_dataclass
import typing

Email = marshmallow_dataclass.NewType('Email', str, field=marshmallow.fields.Email)


@dataclass
class ContactInfo:
    mail: Email = field(default="anonymous@example.org")

ContactInfoSchema = marshmallow_dataclass.class_schema(ContactInfo)()

ContactInfoSchema.load({})
ContactInfo(mail='anonymous@example.org')

ContactInfoSchema.load({"mail": "grumble grumble"})

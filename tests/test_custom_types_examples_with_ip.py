import ipaddress
import unittest
from dataclasses import dataclass, field
from typing import List, Optional

import marshmallow.validate
import marshmallow_dataclass

from marshmallow_dataclass.typing import Email, Url


@dataclass
class Website:
    # field metadata is used to instantiate the marshmallow field
    url: Url = field(default="http://www.example.org")
    contact: Email = field(default="contact@example.org")
    ip: ipaddress.IPv4Address = field(default="127.0.0.1")


WebsiteSchema = marshmallow_dataclass.class_schema(Website)()


class TestWebsiteExample(unittest.TestCase):
    def test_load_defaults(self) -> None:
        default = WebsiteSchema.load({})
        website = Website(
            url="http://www.example.org",
            contact="contact@example.org",
            ip="127.0.0.1",
        )
        self.assertIs(type(website.ip), ipaddress.IPv4Address)
        self.assertEqual(
            default,
            website,
        )

    def test_load(self) -> None:
        google = WebsiteSchema.load(
            {
                "url": "http://www.google.com",
                "contact": "admin@google.com",
                "ip": "216.58.204.110",
            }
        )
        website = Website(
            url="http://www.google.com",
            contact="admin@google.com",
            ip="216.58.204.110",
        )
        self.assertEqual(
            google,
            website,
        )

    def test_back_and_forth(self) -> None:
        original_dict = {
            "url": "http://www.github.com",
            "contact": "admin@github.com",
            "ip": "140.82.121.4",
        }
        github_dict = WebsiteSchema.dump(WebsiteSchema.load(original_dict))
        self.assertEqual(github_dict, original_dict)


if __name__ == "__main__":
    unittest.main()

import unittest
from dataclasses import dataclass, field

import marshmallow_dataclass
from marshmallow_dataclass.typing import Email, Url


@dataclass
class Website:
    # field metadata is used to instantiate the marshmallow field
    url: Url = field(default="http://www.example.org")
    contact: Email = field(default="contact@example.org")


WebsiteSchema = marshmallow_dataclass.class_schema(Website)()


class TestWebsiteExample(unittest.TestCase):
    def test_load_defaults(self) -> None:
        default = WebsiteSchema.load({})
        website = Website(
            url="http://www.example.org",
            contact="contact@example.org",
        )
        self.assertEqual(
            default,
            website,
        )

    def test_load(self) -> None:
        google = WebsiteSchema.load(
            {
                "url": "http://www.google.com",
                "contact": "admin@google.com",
            }
        )
        website = Website(
            url="http://www.google.com",
            contact="admin@google.com",
        )
        self.assertEqual(
            google,
            website,
        )

    def test_back_and_forth(self) -> None:
        original_dict = {
            "url": "http://www.github.com",
            "contact": "admin@github.com",
        }
        github_dict = WebsiteSchema.dump(WebsiteSchema.load(original_dict))
        self.assertEqual(github_dict, original_dict)


if __name__ == "__main__":
    unittest.main()

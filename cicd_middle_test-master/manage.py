#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_gallery.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    def test_image_title(self):
        self.assertEqual(self.image.title, 'Beautiful Landscape')

    def test_image_categories(self):
        self.assertEqual(self.image.categories.count(), 1)
        self.assertEqual(self.image.categories.first(), self.category)

    def test_image_created_date(self):
        self.assertEqual(self.image.created_date, date.today())

    def test_image_age_limit(self):
        self.assertEqual(self.image.age_limit, 18)


if __name__ == '__main__':
    main()

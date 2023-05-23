import datetime
from django.test import TestCase
from models import Category, Image

class ImageTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.image = Image.objects.create(
            title='Test Image',
            image='path/to/test/image.jpg',
            created_date=datetime.date.today(),
            age_limit=18
        )
        self.image.categories.add(self.category)

    def test_image_has_title(self):
        self.assertEqual(self.image.title, 'Test Image')

    def test_image_has_image_path(self):
        self.assertEqual(self.image.image, 'path/to/test/image.jpg')

    def test_image_has_created_date(self):
        self.assertEqual(self.image.created_date, datetime.date.today())

    def test_image_has_age_limit(self):
        self.assertEqual(self.image.age_limit, 18)

    def test_image_has_categories(self):
        self.assertIn(self.category, self.image.categories.all())

    def test_category_has_name(self):
        self.assertEqual(self.category.name, 'Test Category')

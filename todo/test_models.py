from django.test import TestCase
from .models import Item


class TestItemModel(TestCase):
    
    def test_done_defaults_toFalse(self):
        item = Item(name="create a Test")
        item.save()
        self.assertEqual(item.name, "create a Test")
        self.assertFalse(item.done)
        
        
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name="create a Test", done=True)
        item.save()
        self.assertEqual(item.name, "create a Test")
        self.assertTrue(item.done)
    
    def test_item_as_a_string(self):
        item = Item(name="Create a test")
        self.assertEqual("Create a test", str(item))

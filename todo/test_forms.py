from django.test import TestCase
from .forms import ItemForm

class TestToDoItemForm(TestCase):

    def test_can_create_an_item_without_just_a_name(self):
        form = ItemForm({'name': 'Create Tests'})
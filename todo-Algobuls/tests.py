
from django.test import TestCase
from .models import TodoItem

class TodoItemTestCase(TestCase):
    def setUp(self):
        TodoItem.objects.create(
            title="Sample Task",
            description="This is a sample task.",
        )

    def test_todo_creation(self):
        task = TodoItem.objects.get(title="Sample Task")
        self.assertEqual(task.description, "This is a sample task.")

# Create your tests here.

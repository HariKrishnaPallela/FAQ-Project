from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def test_translation(self):
        faq = FAQ.objects.create(
            question_en="Hello",
            answer_en="<p>World</p>"
        )
        self.assertEqual(faq.get_translated('hi')['question'], "नमस्ते")  # Hindi translation
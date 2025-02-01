from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    # Base language (English)
    question_en = models.TextField()
    answer_en = RichTextField()
    
    # Translations (add more languages as needed)
    question_hi = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)
    question_bn = models.TextField(blank=True)
    answer_bn = RichTextField(blank=True)

    def get_translated(self, lang='en'):
        """Retrieve translated text dynamically."""
        return {
            'question': getattr(self, f'question_{lang}', self.question_en),
            'answer': getattr(self, f'answer_{lang}', self.answer_en)
        }

    def save(self, *args, **kwargs):
        """Auto-translate missing fields using Google Translate."""
        translator = Translator()
        languages = ['hi', 'bn']  # Add more languages here
        
        for lang in languages:
            if not getattr(self, f'question_{lang}', None):
                translated = translator.translate(self.question_en, dest=lang)
                setattr(self, f'question_{lang}', translated.text)
            if not getattr(self, f'answer_{lang}', None):
                translated = translator.translate(self.answer_en, dest=lang)
                setattr(self, f'answer_{lang}', translated.text)
        super().save(*args, **kwargs)
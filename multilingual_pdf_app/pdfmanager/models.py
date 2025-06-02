from django.db import models

LANG_CHOICES = [
    ('en', 'English'),
    ('fr', 'French'),
    ('es', 'Spanish'),
]

class PDFDocument(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdfs/')
    language = models.CharField(max_length=10, choices=LANG_CHOICES, default='en')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.language})"

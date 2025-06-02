from django.test import TestCase
from django.urls import reverse
from .models import PDFDocument
from django.core.files.uploadedfile import SimpleUploadedFile

class PDFManagerTests(TestCase):

    def setUp(self):
        # Create a sample PDF file in memory
        self.sample_pdf = SimpleUploadedFile("test.pdf", b"%PDF-1.4 test content", content_type="application/pdf")

    def test_upload_pdf(self):
        response = self.client.post(reverse('pdfmanager:upload_pdf'), {
            'title': 'Test PDF',
            'pdf_file': self.sample_pdf,
            'language': 'en',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(PDFDocument.objects.count(), 1)

    def test_index_view(self):
        response = self.client.get(reverse('pdfmanager:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test PDF")  # if a PDF exists

    def test_translate_text_view(self):
        response = self.client.post(reverse('pdfmanager:translate_text'), {'text': 'Hello', 'target_lang': 'fr'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('translated_text', response.json())

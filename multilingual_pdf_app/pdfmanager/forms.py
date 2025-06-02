from django import forms
from .models import PDFDocument

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title', 'pdf_file', 'language']
        widgets = {
            'language': forms.Select(attrs={'class': 'form-control'}),
        }

class MergePDFsForm(forms.Form):
    pdf_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

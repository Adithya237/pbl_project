import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, FileResponse
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import PDFUploadForm, MergePDFsForm
from .models import PDFDocument

# For PDF generation, merging, translation - stubbed functions (implement in services.py ideally)
from .services import generate_pdf, merge_pdfs, translate_text_content


def index(request):
    """Homepage: Show list of uploaded PDFs and upload form"""
    pdfs = PDFDocument.objects.all().order_by('-uploaded_at')
    form = PDFUploadForm()
    return render(request, 'pdfmanager/index.html', {'pdfs': pdfs, 'form': form})


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdfmanager:index')
    else:
        form = PDFUploadForm()
    return render(request, 'pdfmanager/upload.html', {'form': form})


def preview_pdf(request, pk):
    """Show side-by-side original and translated PDF previews"""
    pdf = get_object_or_404(PDFDocument, pk=pk)
    # Generate translated PDF on the fly (stub)
    translated_pdf_path = generate_pdf(language='fr', content='Dummy content for preview')  # Replace with real data
    
    context = {
        'original_pdf_url': pdf.pdf_file.url,
        'translated_pdf_url': translated_pdf_path,
        'pdf': pdf,
    }
    return render(request, 'pdfmanager/preview.html', context)


def merge_pdfs(request):
    if request.method == 'POST':
        form = MergePDFsForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('pdf_files')
            merged_pdf_path = merge_pdfs(files)
            # Serve merged PDF as file response or redirect to download page
            return FileResponse(open(merged_pdf_path, 'rb'), as_attachment=True, filename='merged.pdf')
    else:
        form = MergePDFsForm()
    return render(request, 'pdfmanager/merge.html', {'form': form})


def download_pdf(request, pk):
    pdf = get_object_or_404(PDFDocument, pk=pk)
    file_path = pdf.pdf_file.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))


@csrf_exempt
def translate_text(request):
    """
    AJAX endpoint for real-time translation.
    Expects POST with 'text' and 'target_lang'.
    """
    if request.method == 'POST':
        text = request.POST.get('text', '')
        target_lang = request.POST.get('target_lang', 'en')
        translated = translate_text_content(text, target_lang)
        return JsonResponse({'translated_text': translated})
    return JsonResponse({'error': 'Invalid request'}, status=400)

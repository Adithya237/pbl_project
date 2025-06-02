from django.urls import path
from . import views

app_name = 'pdfmanager'

urlpatterns = [
    path('', views.index, name='index'),  # Homepage: upload & manage PDFs
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('preview/<int:pk>/', views.preview_pdf, name='preview_pdf'),
    path('merge/', views.merge_pdfs, name='merge_pdfs'),
    path('download/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('translate/', views.translate_text, name='translate_text'),  # Ajax for real-time translation
]

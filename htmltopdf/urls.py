from django.urls import path
from htmltopdf import views

app_name='converter'

urlpatterns = [
    path('manual_resume',views.manual_resume.as_view(),name='manual'),
	path('template_sel/<int:from_index>/',views.template.as_view(),name='select'),
	path('<int:temp_index>/', views.fork.as_view(),name='fork'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]

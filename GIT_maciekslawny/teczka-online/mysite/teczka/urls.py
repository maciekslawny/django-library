from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'teczka'

urlpatterns = [
    path('', views.cases_list, name='cases_list'),
    path('ended', views.cases_list_ended, name='cases_list_ended'),
    path('case-detail/<int:case_id>', views.case_detail, name='case_detail'),
    path('delete-document/<int:case_id>/<int:document_id>', views.delete_document, name='delete_document'),
    path('add-case/', views.add_case, name='add_case'),
    path('edit-case/<int:case_id>', views.edit_case, name='edit_case'),
    path('generate-pdf/<int:case_id>', views.generate_pdf, name='generate_pdf'),
    path('delete-case/<int:case_id>', views.delete_case, name='delete_case'),
    path('zaladunki', views.cases_list_loading_date, name='cases_list_loading_date'),
    path('upload', views.upload, name='upload'),
    path('test-page', views.test_page, name='test_page'),
    path('ustawienia', views.settings, name='settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
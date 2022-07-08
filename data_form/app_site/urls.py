from django.urls import path

from app_site.views import get_all_forms_empty, get_one_form_for_fill, get_all_forms_not_empty, get_one_form_detail

urlpatterns = [
    path('', get_all_forms_empty, name='site_form_list_empty'),
    path('get_not_empty/', get_all_forms_not_empty, name='site_form_list_not_empty'),
    path('add_data/<int:pk>/', get_one_form_for_fill, name='add_data'),
    path('add_data/', get_all_forms_empty, name='site_form_list_empty'),
    path('detail/<int:pk>/', get_one_form_detail, name='site_form_detail')
]

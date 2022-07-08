from django.urls import path

from app_data.api import DataFormViewSet, DataFormViewDetail
from app_data.views import DataFormListView, DataFormCreateView, update_form_view


urlpatterns = [
    path('', DataFormListView.as_view(), name='data_form_list'),
    path('create/', DataFormCreateView.as_view(), name='data_form_create'),
    path('<int:data_form_id>/edit', update_form_view, name='data_form_edit'),
    path('api/', DataFormViewSet.as_view(), name='api'),
    path('api/detail/<int:pk>/', DataFormViewDetail.as_view(), name='api_update'),
]

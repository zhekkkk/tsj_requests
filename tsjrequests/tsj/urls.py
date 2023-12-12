from django.urls import path
from . import views
from .views import AjaxUpdateView

urlpatterns = [
    path('', views.show_requests, name='home'),
    path('workers/', views.show_workers, name='workers'),
    path('residents/', views.show_residents, name='residents'),
    path('requests/', views.show_requests, name='requests'),
    path('apartments/', views.show_apartments, name='apartments'),
    path('addresses/', views.show_addresses, name='addresses'),
    # path('requests/<int:req_id>', views.show_request, name='request'),
    path('requests/<slug:type_slug>', views.show_request_by_type, name='request_type'),
    path('create-address/', views.update_address, name='create_address'),
    path('update-address/<int:address_id>', views.update_address, name='update_address'),
    path('delete-address/<int:address_id>', views.delete_address, name='delete_address'),
    path('create-worker/', views.update_worker, name='create_worker'),
    path('update-worker/<int:worker_id>', views.update_worker, name='update_worker'),
    path('delete-worker/<int:worker_id>', views.delete_worker, name='delete_worker'),
    path('create-request/', views.update_request, name='create_request'),
    path('update-request/<int:request_id>', views.update_request, name='update_request'),
    path('delete-request/<int:request_id>', views.delete_request, name='delete_request'),
    path('create-resident/', views.update_resident, name='create_resident'),
    path('update-resident/<int:resident_id>', views.update_resident, name='update_resident'),
    path('delete-resident/<int:resident_id>', views.delete_resident, name='delete_resident'),
    path('create-apartment/', views.update_apartment, name='create_apartment'),
    path('update-apartment/<int:apartment_id>', views.update_apartment, name='update_apartment'),
    path('delete-apartment/<int:apartment_id>', views.delete_apartment, name='delete_apartment'),
    path('workers/<slug:position_slug>', views.show_worker_by_position, name='worker_position'),
    path('work-types/<int:work_position_id>', views.show_work_types, name='home'),
    path('ajax-update/', AjaxUpdateView.as_view(), name='ajax_update')
]
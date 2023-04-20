from django.urls import path
from admin_dashboard.views import *

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('login', admin_sign_in_view, name='admin_login'),
    path('logout', admin_sign_out_view, name='admin_logout'),

    path('site-info', SiteInfoView.as_view(), name='site_info'),
    path('site-info/create', SiteInfoCreateView.as_view(), name='site_info_create'),
    path('site-info/<int:pk>/update', SiteInfoUpdateView.as_view(), name='site_info_update'),

    path('gallery/add', GalleryCreateView.as_view(), name='gallery_create'),
    path('gallery/index', GalleryListView.as_view(), name='gallery_index'),
    path('gallery/<int:pk>/delete', GalleryDeleteView.as_view(), name='gallery_delete'),


]


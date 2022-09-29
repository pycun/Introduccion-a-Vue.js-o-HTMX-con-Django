from django.urls import path
from django.views import generic

from src.apps.refugio import views

urlpatterns = [
    path('mascota/list/', views.MascotaListview.as_view(), name='mascota_list'),
    path('mascota/create/', views.MascotaCreateView.as_view(), name='mascota_create'),
    path('mascota/<slug:pk>/', views.MascotaDetailView.as_view(), name='mascota_detail'),
    path('mascota/<slug:pk>/update/', views.MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascota/<slug:pk>/delete/', views.MascotaDeleteView.as_view(), name='mascota_delete'),

    path('vue/', views.VueView.as_view(), name='vue'),
    path('vue/<path:path>/', views.VueView.as_view(), name='vue'),

    path('vue-min/', views.VueMinListView.as_view(), name='vue_min_list'),
    path('vue-min/<int:pk>/', views.VueMinUpdateView.as_view(), name='vue_min_edit'),

    path('htmx/intro/clicked/', generic.TemplateView.as_view(template_name='htmx/intro.html')),
    path('htmx/intro/mouseenter/', generic.TemplateView.as_view(template_name='htmx/intro.html')),

    path('htmx/', views.HTMXListView.as_view(), name='htmx_list'),
    path('htmx/<int:pk>', views.HTMXDetailView.as_view(), name='htmx_detail'),
    path('htmx/<int:pk>/update/', views.HTMXUpdateView.as_view(), name='htmx_update'),

]
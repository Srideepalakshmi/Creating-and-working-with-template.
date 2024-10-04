from django.urls import path
from . import views
urlpatterns = [
    path('oddfilter/', views.oddfilter, name='oddfilter'),  # Maps /filter/ URL to the filter_names view
]

from django.contrib import admin
from django.urls import path
from ex2app import views as ex2app_views  # Import views from ex2app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('oddfilter/', ex2app_views.oddfilter, name='oddfilter'),  # Route for the odd view
   ]

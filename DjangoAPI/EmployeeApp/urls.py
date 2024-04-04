from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from EmployeeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.departmentApi),  # Redirect root URL to departmentApi view
    path('department', views.departmentApi),
    re_path(r'^department/([0-9]+)$', views.departmentApi),
    path('employee', views.employeeApi),
    re_path(r'^employee/([0-9]+)$', views.employeeApi),
    path('employee/savefile', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path("testimonials/",testimonials),
    path("feedback/",feedback)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
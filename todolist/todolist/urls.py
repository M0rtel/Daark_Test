from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include('rest_framework.urls')),
    path("api/", include('lists.api.urls', namespace='api')),
    path("", include('lists.urls', namespace='lists')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from profiles.views import home_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),
]

handler404 = 'profiles.views.custom_404'

# Serve static and media files unconditionally for local development/testing
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
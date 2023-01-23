from django.conf.urls.static import static
from django.urls import path

from config import settings
from .views import NewsHome
from .views import show_post

urlpatterns = [
    path('', NewsHome.as_view(), name='news'),
    path('post/<int:post_id>/', show_post, name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT
                          )

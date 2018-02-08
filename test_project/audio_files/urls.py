from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static

from .views import AudioFileAPICreateView, AudioFileCRUDCreateView

urlpatterns = [
    re_path(r'^audio-files/$',
        AudioFileAPICreateView.as_view(create_field='audio_file'),
        name='audio-file-api-create'),
    re_path(r'^audio-files/new$',
        AudioFileCRUDCreateView.as_view(),
        name='audio-file-crud-create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

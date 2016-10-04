from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
from blog.views import *


urlpatterns = [
    # url(r'^$', PrefaceList.as_view(), name='sidebar'),
    url(r'^$', index, name='index'),
    url(r'^main/', include('main.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

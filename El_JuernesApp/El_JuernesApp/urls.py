from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [

                  path('admin/', admin.site.urls),
                  url(r'^accounts/', include('Accounts.urls')),
                  path('', TemplateView.as_view(template_name="Home_News.html"), name="Home_News"),
                  path('AFE/', include('AfeNews.urls')),
                  path('Redactor/', include('Copywriter.urls')),
                  path('Reporter_grafic/', include('Graphic_reporter.urls')),
                  path('Maquetador/', include('Layout_designer.urls')),
                  path('access_denegat/', TemplateView.as_view(template_name="access_denied.html"),
                       name="access_denied"),

                  path('Redactor_cap/', include('HeadCopywriter.urls')),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


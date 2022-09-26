from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from drf_yasg.views import get_schema_view as swagger_get_schema_view
# from drf_yasg import openapi

# schema_view = swagger_get_schema_view(
#    openapi.Info(
#       title="Resume API",
#       default_version='v1',
#       description="Get all the endpoints for this Resume REST app",
#    ),
#    public=True,
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

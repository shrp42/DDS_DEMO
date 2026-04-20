from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from item import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('items/', include('item.urls', namespace='item')),
    path('api/items/', views.api_items_list, name='api_items'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

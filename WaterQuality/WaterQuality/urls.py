from django.contrib import admin
from django.urls import path
from myapp.views import predict_water_quality
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', views.predict_water_quality, name='predict'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Hate Speech Sentiment Analysis API",
      default_version='v1',
      description="Hate Speech Sentiment API",
      terms_of_service="https://www.plexaar.com/policies/terms/",
      contact=openapi.Contact(email="adnanmajeed82@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sentiment_analysis_app.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

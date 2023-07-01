"""
URL configuration for pereval project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from perevalapp.views import SubmitDataDetailView, SubmitDataUpdateView, SubmitDataListView

from rest_framework import routers, permissions
from rest_framework.schemas.views import SchemaView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

api_info = openapi.Info(
    title="Snippets API",
    default_version="v1",
)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/submit-data', include('perevalapp.urls')),
    path('api/v1/submit-data', include('rest_framework.urls')),
    path('api/v1/submit-data', SubmitDataListView.as_view(), name='submit-data-list'),
    path('api/v1/submit-data/1/', SubmitDataDetailView.as_view(), name='submit-data-detail'),
    path('api/v1/submit-data/1/', SubmitDataUpdateView.as_view(), name='submit-data-update'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include("pereval.urls")),

]

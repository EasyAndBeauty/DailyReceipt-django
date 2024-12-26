"""
URL configuration for dailyreceipt_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


def index(request):
    return HttpResponse("Welcome to DailyReceipt API")

schema_view = get_schema_view(
    openapi.Info(
        title="DailyReceipt API",
        default_version='v1',
        description="DailyReceipt API documentation",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="dndb3599@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # swagger 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # admin
    path("admin/", admin.site.urls),

    # index
    path("", index),

    # api
    path("api/", include([
        
        # auth
        path("auth/", include("authentication.urls")),
    ])),
]

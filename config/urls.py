"""si_tower URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
# from apps.api.urls import router
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_jwt.views import obtain_jwt_token
from django.views.generic import TemplateView #追加


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.commons.urls')),
    path('', include('apps.accounts.urls')),
    path('', include('apps.pms.urls')),
    # path('', include('apps.api.urls')),
    # path('api/', include(router.urls)),
    path('api/', include('apps.api.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api-auth/', obtain_jwt_token),

    path('', TemplateView.as_view(template_name='index.html'), name='home'), # 追加
    path('accounts/', include('allauth.urls')), # 追加
]

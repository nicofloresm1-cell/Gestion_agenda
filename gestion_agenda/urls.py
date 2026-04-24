from django.contrib import admin
from django.urls import path, include
from agenda import views as agenda_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agenda.urls', namespace='agenda')),
    path('accounts/signup/', agenda_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('agenda.api_urls')),

    path('api/login/', TokenObtainPairView.as_view(), name='api_login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='api_refresh'),
]
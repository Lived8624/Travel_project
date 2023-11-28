from travelproject import settings
from . import views
from django.conf.urls.static import static
from django.urls import path, include

# Create your views here.
urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout,name='logout')

]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

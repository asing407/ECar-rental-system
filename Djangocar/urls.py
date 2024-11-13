from django.contrib import admin
from django.urls import path, include  # 确保你导入了 include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('carrent.urls')),
]
"""utkarshOdisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

# chnage text of admin/database page -----    start

admin.site.site_header = "Utkarsh-Odisha Admin"
admin.site.index_title = "Utkarsh-Odisha admin portak"
admin.site.site_title = "welcome to Utkarsh-Odisha"

# chnage text of admin/database page -----    end

urlpatterns = [
    path('admin/', admin.site.urls),

    # go to urls.py of home
    path('', include('home.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

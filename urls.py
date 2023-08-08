"""
URL configuration for socialnet project.

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
from django.urls import path
from core.views import homepage, contacts, about_us, short_info,shorts, Categories, Category_info, video

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('shop/contacts/', contacts),
    path('shop/about_us/', about_us),
    path('short/<int:id>',short_info),
    path('shorts',shorts),
    path('short.video.url/<int:id>',video),
    path('category/<int:id>',Category_info),
    path('categories',Categories),
]
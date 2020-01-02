"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from . import api
from django.conf.urls.static import static
from django.conf import settings
# #talako import feeds hernako lagi
# from django.conf.urls import *
# from feeds import LatestEntries, LatestEntriesByCategory
# feeds = {
#     'latest': LatestEntries,
#     'categories': LatestEntriesByCategory,
# }

# urlpatterns = patterns('',
#     (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
#         {'feed_dict': feeds}),
# )
# #yeha samma feed ko



urlpatterns = [
    path('admin/', admin.site.urls),
    path("layout/", include("mainApp.urls")),
    path("about/", include("about.urls")),
    path("contact/", include("contact.urls")),
    path('api/v1/', include(api.router.urls)),
    path('login/',include("login.urls")),
    path('',include("home.urls")),
    path("product/", include("product.urls")),
    path('product_detail/', include('product_detail.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('order_complete/', include('order_complete.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


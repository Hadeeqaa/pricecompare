from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from compare.views import search_products, home, results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('results/', results, name='results'),
    path('api/search/', search_products),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
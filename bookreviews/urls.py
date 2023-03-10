from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from book import views as bookViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", bookViews.home, name="home"),
    path("about/", bookViews.about, name="about"),
    path("signup/", bookViews.signup, name="signup"),
    path("news/", include("news.urls")),
    path('book/', include('book.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
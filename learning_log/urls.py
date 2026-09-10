from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
path("admin/", admin.site.urls),


path("", include("learning_logs.urls")),
path("accounts/", include("accounts.urls")),

path(
    "robots.txt",
    TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain"
    ),
),

path(
    "sitemap.xml",
    TemplateView.as_view(
        template_name="sitemap.xml",
        content_type="application/xml"
    ),
),


]

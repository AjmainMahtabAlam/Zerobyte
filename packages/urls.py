from django.urls import path
from .views import PackageListCreateView, PackageDetailView, PackageSoftDeleteView, PackageRestoreView

urlpatterns = [
    path("packages/", PackageListCreateView.as_view(), name="package-list"),
    path("packages/<int:pk>/", PackageDetailView.as_view(), name="package-detail"),
    path("packages/<int:pk>/delete/", PackageSoftDeleteView.as_view(), name="package-delete"),
    path("packages/<int:pk>/restore/", PackageRestoreView.as_view(), name="package-restore"),
]

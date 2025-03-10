from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Package
from .serializers import PackageSerializer

class PackageListCreateView(generics.ListCreateAPIView):
    queryset = Package.objects.filter(is_deleted=False)  # Exclude soft deleted
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]

class PackageDetailView(generics.RetrieveUpdateAPIView):
    queryset = Package.objects.filter(is_deleted=False)
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]

class PackageSoftDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, format=None):
        try:
            package = Package.objects.get(pk=pk, is_deleted=False)
            package.delete()
            return Response({"message": "Package soft deleted"}, status=204)
        except Package.DoesNotExist:
            return Response({"error": "Package not found"}, status=404)

class PackageRestoreView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        try:
            package = Package.objects.get(pk=pk, is_deleted=True)
            package.restore()
            return Response({"message": "Package restored"})
        except Package.DoesNotExist:
            return Response({"error": "Package not found"}, status=404)

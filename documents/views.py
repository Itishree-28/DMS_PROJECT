from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
import os

from .models import DocumentManagement
from .serializers import DocumentSerializer
from users.permissions import HasModulePermission


class DocumentViewSet(ModelViewSet):
    queryset = DocumentManagement.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    module = "Admin"
    submodule = "Documents"

    # Get all documents of a specific user
    @action(detail=False, methods=["GET"], url_path="user/(?P<user_id>[^/.]+)")
    def documents_by_user(self, request, user_id=None):
        docs = DocumentManagement.objects.filter(user_id=user_id)
        return Response(DocumentSerializer(docs, many=True).data)

    # Download document
    @action(detail=True, methods=["GET"], url_path="download")
    def download(self, request, pk=None):
        doc = self.get_object()
        if not os.path.exists(doc.file_path.path):
            return Response({"error": "File not found"}, status=404)

        return FileResponse(open(doc.file_path.path, "rb"), as_attachment=True)

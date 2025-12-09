from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import InternalChat
from .serializers import InternalChatSerializer
from users.permissions import HasModulePermission


class InternalChatViewSet(ModelViewSet):
    queryset = InternalChat.objects.all()
    serializer_class = InternalChatSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]

    # RBAC module & submodule
    module = "Admin"
    submodule = "Chat"

    # Get chat history between 2 users
    @action(detail=False, methods=["GET"], url_path="history/(?P<user1>[^/.]+)/(?P<user2>[^/.]+)")
    def chat_history(self, request, user1=None, user2=None):
        msgs = InternalChat.objects.filter(
            sender_id__in=[user1, user2],
            receiver_id__in=[user1, user2]
        ).order_by("timestamp")

        return Response(InternalChatSerializer(msgs, many=True).data)

    # Mark messages as read
    @action(detail=False, methods=["POST"], url_path="mark-read/(?P<message_id>[^/.]+)")
    def mark_read(self, request, message_id=None):
        try:
            msg = InternalChat.objects.get(id=message_id)
            msg.read_status = True
            msg.save()
            return Response({"status": "marked as read"})
        except InternalChat.DoesNotExist:
            return Response({"error": "Message not found"}, status=404)

    # Get unread messages for the logged-in user
    @action(detail=False, methods=["GET"], url_path="unread")
    def unread_messages(self, request):
        user_id = request.user.id
        msgs = InternalChat.objects.filter(receiver_id=user_id, read_status=False)
        return Response(InternalChatSerializer(msgs, many=True).data)

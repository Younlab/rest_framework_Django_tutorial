from django.contrib.auth import get_user_model

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics

__all__ = (
    'SnippetList',
    'SnippetDetail',
    'UserList',
    'UserDetail',
)

User = get_user_model()

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        # SnippetSerializer 로 전달받은 데이터에
        # 'owner' 항목에 self.request.user 데이터를 추가한 후
        # save() 호출, DB 에 저장 및 인스턴스 반환
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
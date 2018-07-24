from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Snippet

__all__ =(
    'SnippetSerializer',
)

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'snippets',
        )


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'pk',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'owner',
        )
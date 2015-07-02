from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    serializer = UserSerializer(request.user)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details_by_username(request, username=None):
    username_user = get_user_model().objects.filter(username=username).first()

    if username and username == request.user:
        serializer = UserSerializer(request.user)

        return Response(serializer.data)
    else:
        return Response({'details': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

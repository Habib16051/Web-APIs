from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializers, UserSerailizers
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import viewsets


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthorOrReadOnly, ]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthorOrReadOnly, ]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# Viewsets - One viewset can replace multiple views.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser,]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerailizers


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerailizers


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerailizers

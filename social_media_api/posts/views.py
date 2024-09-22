from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

# View to like a post
@api_view(['POST'])
def like_post(request, pk):
    # Use get_object_or_404 to retrieve the post or return 404 if not found
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Use get_or_create to like the post
    like, created = Like.objects.get_or_create(user=user, post=post)

    if created:
        # If the like is created, notify the post author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target=post
        )
        return Response({'detail': 'Post liked.'}, status=status.HTTP_201_CREATED)

    # If the user has already liked the post
    return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

# View to unlike a post
@api_view(['POST'])
def unlike_post(request, pk):
    # Use get_object_or_404 to retrieve the post
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Try to get the Like object, and delete it if found
    like = Like.objects.filter(user=user, post=post).first()

    if like:
        like.delete()
        return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)

    return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

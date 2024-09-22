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


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    # Check if the user has already liked the post
    if Like.objects.filter(user=user, post=post).exists():
        return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a like
    like = Like.objects.create(user=user, post=post)

    # Create a notification for the post author
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked your post',
        target=post
    )

    return Response({'detail': 'Post liked.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    # Check if the user has liked the post
    try:
        like = Like.objects.get(user=user, post=post)
        like.delete()
        return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

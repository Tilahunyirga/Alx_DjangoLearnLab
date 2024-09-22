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

Post.objects.filter(author__in=following_users).order_by 
following.all()

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from .serializers import PostSerializer
from notifications.models import Notification

# Like a post
@api_view(['POST'])
def like_post(request, pk):
    # Get the post or return 404 if not found
    post = get_object_or_404(Post, pk=pk)
    
    # Get the user from the request
    user = request.user

    # Check if the user has already liked the post, if not, create the like
    like, created = Like.objects.get_or_create(user=user, post=post)

    if created:
        # If a new like was created, trigger a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target=post
        )
        return Response({'detail': 'Post liked.'}, status=status.HTTP_201_CREATED)
    
    # If the user already liked the post, inform them
    return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

# Unlike a post
@api_view(['POST'])
def unlike_post(request, pk):
    # Get the post or return 404 if not found
    post = get_object_or_404(Post, pk=pk)

    # Get the user from the request
    user = request.user

    # Try to get the Like object if it exists
    like = Like.objects.filter(user=user, post=post).first()

    if like:
        # If the like exists, delete it
        like.delete()
        return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)
    
    # If no like exists, inform the user
    return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404  # Ensure this is imported
from .models import Post, Like  # Import your Post and Like models

# Like a post
@api_view(['POST'])
def like_post(request, pk):
    # Retrieve the post using get_object_or_404, ensuring 404 if not found
    post = get_object_or_404(Post, pk=pk)
    
    # Get the user from the request
    user = request.user

    # Use Like.objects.get_or_create() to either get an existing like or create a new one
    like, created = Like.objects.get_or_create(user=user, post=post)

    if created:
        # If the like was created (i.e., the user is liking the post for the first time)
        return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)
    
    # If the like already exists (i.e., the user has already liked the post)
    return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

# Unlike a post
@api_view(['POST'])
def unlike_post(request, pk):
    # Retrieve the post using get_object_or_404, ensuring 404 if not found
    post = get_object_or_404(Post, pk=pk)

    # Get the user from the request
    user = request.user

    # Check if the Like object exists for the given user and post
    like = Like.objects.filter(user=user, post=post).first()

    if like:
        # If the like exists, delete it (
generics.get_object_or_404(Post, pk=pk),
Like.objects.get_or_create(user=request.user, post=post)
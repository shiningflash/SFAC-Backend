from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from job_post.models import JobPost, Like
from .serializers import JobPostSerializer, LikeSerializer


class JobPostList(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
       
        
class JobPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    
    def delete(self, request, *args, **kwargs):
        post = JobPost.objects.filter(pk=kwargs['pk'], poster=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This isn\'t your post to delete ...')
 
        
class CreateLike(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        post = JobPost.objects.get(pk=self.kwargs['pk'])
        return Like.objects.filter(liker=user, post=post)
    
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already liked for this post :)')
        serializer.save(liker=self.request.user, post=JobPost.objects.get(pk=self.kwargs['pk']))
        
    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never liked for this post!!!')
from rest_framework import serializers

from job_post.models import JobPost, Like


class JobPostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.first_name')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    likes = serializers.SerializerMethodField()
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    
    class Meta:
        model = JobPost
        fields = ['id', 'position', 'company', 'salary', 'experience',
                  'url', 'description', 'poster', 'poster_id', 'created_at', 'updated_at']
        
    def get_likes(self, post):
        return Like.objects.filter(post=post).count()
    

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'liker', 'created_at']
        
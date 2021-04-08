from django.db import models

from account.models import Account


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return self.updated_at
    

class JobPost(BaseModel):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    salary = models.FloatField(null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    url = models.URLField()
    description = models.TextField(max_length=5000)
    poster = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['position', '-salary', 'company']
    
    def __str__(self):
        return f'{self.position}, {self.company}'
    

class Like(BaseModel):
    liker = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    post = models.ForeignKey('job_post.JobPost', on_delete=models.CASCADE)
    
    class Meta:
        pass
    
    def __str__(self):
        return f'{self.liker} : {self.post}'
    
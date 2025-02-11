from django.db import models

# Create your models here.
# This is for your DB design. Models simplify the database design so we dont have to keep going back and forth with SQL

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=20, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False) # Check for wrong answer
    
    def __str__(self):
        return self.text


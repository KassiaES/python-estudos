from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    creat_at = models.DateField(auto_now_add=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.text
    
class Option(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

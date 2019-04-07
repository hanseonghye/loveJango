from django.db import models

class Question(models.Models):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DataTimeField('date published')

    def __str__(self):
        return self.question_text

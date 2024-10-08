from django.db import models

class Note(models.Model):
    note_id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

class Email(models.Model):
    sender = models.EmailField()
    receiver = models.EmailField()
    cc = models.CharField(max_length=1000, blank=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return self.subject

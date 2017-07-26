from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(default='python', max_length=100)
    style = models.CharField(default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', null=True, blank=True)
    highlighted = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

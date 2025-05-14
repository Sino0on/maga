from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Test(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    image = models.FileField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tests')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']


class Question(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)
    answer = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f'{self.title}'


class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='results')
    fullname = models.CharField(max_length=255)
    result = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fullname}'



from django.db import models


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.cat_name


class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news')
    description = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

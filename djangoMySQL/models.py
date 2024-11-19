from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        db_table = 'book'  # Specify the custom table name, default <appname>_<tablename>

    # def __str__(self):
    #     return self.title
    #

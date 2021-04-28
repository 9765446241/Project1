from django.db import models

# Create your models here.
class Book(models.Model):
    #id is created by django default 
    name = models.CharField(max_length=100)
    author =  models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()

# appname_modelname  - small case
# create table book_book (id int unique AUTO_INCREMENT, name varchar(100), author varchar(100), qty int, price float)
    def __str__(self):
        return f"{self.name} ---{self.auther}"

    class Meta:
        db_table = "bookinfo"








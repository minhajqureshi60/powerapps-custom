from django.db import models
# Create your models here.


class Menu(models.Model):
    name=models.CharField(max_length=50)
    parent=models.ForeignKey('self',null=True,blank=True,related_name='children',on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    

class Purchase(models.Model):
    date = models.DateField()
    number_of_bottles = models.IntegerField()
    rupees = models.DecimalField(max_digits=10, decimal_places=2)



    
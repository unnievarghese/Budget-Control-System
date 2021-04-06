from django.db import models

class category(models.Model):
    category_name=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.category_name

class expense(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    notes=models.CharField(max_length=250,null=True)
    amount=models.IntegerField()
    user=models.CharField(max_length=120)
    date=models.DateField()

    def __str__(self):
        return self.amount


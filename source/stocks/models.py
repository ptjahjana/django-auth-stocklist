from django.db import models

class Fabric(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Stock(models.Model):
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    fab_id = models.IntegerField(null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    lot_no = models.CharField(max_length=50, null=True)
    width = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    net_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    lab_no = models.CharField(max_length=50)
    weight_unit = models.CharField(max_length=5, null=True)

    def __str__(self):
        return f"{self.fabric.name} : {self.color.name}"
from django.db import models
from django.conf import settings

class GoodsType(models.Model):
    name = models.CharField(max_length=60)
    addr = models.CharField(max_length=30)
    imageLink = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class GoodsCategory(models.Model):
    linkT = models.ForeignKey('GoodsType', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=60)
    addr = models.CharField(max_length=30)
    def __str__(self):
        return self.linkT.name + " / " + self.name

class Good(models.Model):
    linkT = models.ForeignKey('GoodsType', on_delete=models.SET_NULL, null=True)
    linkC = models.ForeignKey('GoodsCategory', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    dateAdded = models.DateField(null=True, blank=True)
    imageLink = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=14)
    def __str__(self):
        return self.name    

class Cart(models.Model):
    linkU = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    linkG = models.ForeignKey('Good', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=14)
    def __str__(self):
        return self.name    

class gComment(models.Model):
    linkG = models.ForeignKey('Good', on_delete=models.CASCADE, null=True)
    dateAdded = models.DateTimeField(null=True, blank=True)
    linkU = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    def __str__(self):
        return self.comment
    class Meta:
        ordering = ["-dateAdded"]

#	GoodsType(name:string, addr(для ссылки):string)
#	GoodsCategory(linkT(GoodsType), name:string, addr(для ссылки):string)
#	Goods(linkT(GoodsType), linkC(GoodsCategory), name, dateAdded:date, imageLink:string, price:14.2, other props...)
#	Carts(linkU(user), linkG(goods), price:14.2)
#   gComment(linkG(good), dateAdded, linkU(ures), comment:string)
#	- подключить к админке
#	- сделать каталог для картинок
#	- ввести хотя-бы 15-20 примеров товаров
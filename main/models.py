from django.db import models

# Create your models here.


class Elan(models.Model):
    sirket = models.CharField(max_length=100)
    maas = models.CharField(max_length=50)
    seher = models.CharField(max_length=50)
    mezmun = models.CharField(max_length=200)    
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    text1 = models.TextField(max_length=500,null=True) 
    text2 = models.TextField(max_length=500,null=True)  
    text3 = models.TextField(max_length=500,null=True)  
    text4 = models.TextField(max_length=500,null=True)  
    text5 = models.TextField(max_length=500,null=True) 
    text_1 = models.TextField(max_length=500,null=True) 
    text_2 = models.TextField(max_length=500,null=True)  
    text_3 = models.TextField(max_length=500,null=True)  
    text_4 = models.TextField(max_length=500,null=True)  
    text_5 = models.TextField(max_length=500,null=True)  

    staj = models.CharField(max_length=100)
    yash = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    rejm = models.TextField(max_length=250)
    muqavile = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.sirket
    def get_absolute_url(self):
        return f'/'
    
class IT(models.Model):
    sirket = models.CharField(max_length=100)
    maas = models.CharField(max_length=50)
    seher = models.CharField(max_length=50)
    mezmun = models.CharField(max_length=200)    
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    text1 = models.TextField(max_length=500,null=True) 
    text2 = models.TextField(max_length=500,null=True)  
    text3 = models.TextField(max_length=500,null=True)  
    text4 = models.TextField(max_length=500,null=True)  
    text5 = models.TextField(max_length=500,null=True)
    text6 = models.TextField(max_length=500,null=True) 
    text7 = models.TextField(max_length=500,null=True) 

    text_1 = models.TextField(max_length=500,null=True) 
    text_2 = models.TextField(max_length=500,null=True)  
    text_3 = models.TextField(max_length=500,null=True)  
    text_4 = models.TextField(max_length=500,null=True)  
    text_5 = models.TextField(max_length=500,null=True)  
    text_6 = models.TextField(max_length=500,null=True)  
    text_7 = models.TextField(max_length=500,null=True)  

    staj = models.CharField(max_length=100)
    yash = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    rejm = models.TextField(max_length=250)
    muqavile = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.sirket
    def get_absolute_url(self):
        return f'/'
    
class Senaye(models.Model):
    sirket = models.CharField(max_length=100)
    maas = models.CharField(max_length=50)
    seher = models.CharField(max_length=50)
    mezmun = models.CharField(max_length=200)    
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    text1 = models.TextField(max_length=500,null=True) 
    text2 = models.TextField(max_length=500,null=True)  
    text3 = models.TextField(max_length=500,null=True)  
    text4 = models.TextField(max_length=500,null=True)  
    text5 = models.TextField(max_length=500,null=True) 
    text_1 = models.TextField(max_length=500,null=True) 
    text_2 = models.TextField(max_length=500,null=True)  
    text_3 = models.TextField(max_length=500,null=True)  
    text_4 = models.TextField(max_length=500,null=True)  
    text_5 = models.TextField(max_length=500,null=True)  

    staj = models.CharField(max_length=100)
    yash = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    rejm = models.TextField(max_length=250)
    muqavile = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.sirket
    def get_absolute_url(self):
        return f'/'
    
class Security(models.Model):
    sirket = models.CharField(max_length=100)
    maas = models.CharField(max_length=50)
    seher = models.CharField(max_length=50)
    mezmun = models.CharField(max_length=200)    
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    text1 = models.TextField(max_length=500,null=True) 
    text2 = models.TextField(max_length=500,null=True)  
    text3 = models.TextField(max_length=500,null=True)  
    text4 = models.TextField(max_length=500,null=True)  
    text5 = models.TextField(max_length=500,null=True) 
    text_1 = models.TextField(max_length=500,null=True) 
    text_2 = models.TextField(max_length=500,null=True)  
    text_3 = models.TextField(max_length=500,null=True)  
    text_4 = models.TextField(max_length=500,null=True)  
    text_5 = models.TextField(max_length=500,null=True)  

    staj = models.CharField(max_length=100)
    yash = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    rejm = models.TextField(max_length=250)
    muqavile = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.sirket
    def get_absolute_url(self):
        return f'/'
    
class Neqliyyat(models.Model):
    sirket = models.CharField(max_length=100)
    maas = models.CharField(max_length=50)
    seher = models.CharField(max_length=50)
    mezmun = models.CharField(max_length=200)    
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    text1 = models.TextField(max_length=500,null=True) 
    text2 = models.TextField(max_length=500,null=True)  
    text3 = models.TextField(max_length=500,null=True)  
    text4 = models.TextField(max_length=500,null=True)  
    text5 = models.TextField(max_length=500,null=True) 
    text_1 = models.TextField(max_length=500,null=True) 
    text_2 = models.TextField(max_length=500,null=True)  
    text_3 = models.TextField(max_length=500,null=True)  
    text_4 = models.TextField(max_length=500,null=True)  
    text_5 = models.TextField(max_length=500,null=True)  

    staj = models.CharField(max_length=100)
    yash = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    rejm = models.TextField(max_length=250)
    muqavile = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.sirket
    def get_absolute_url(self):
        return f'/'
    
class Tibb(models.Model):
    sirket = models.CharField(max_length=100)
    maas = models.CharField(max_length=50)
    seher = models.CharField(max_length=50)
    mezmun = models.CharField(max_length=200)    
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    text1 = models.TextField(max_length=500,null=True) 
    text2 = models.TextField(max_length=500,null=True)  
    text3 = models.TextField(max_length=500,null=True)  
    text4 = models.TextField(max_length=500,null=True)  
    text5 = models.TextField(max_length=500,null=True) 
    text_1 = models.TextField(max_length=500,null=True) 
    text_2 = models.TextField(max_length=500,null=True)  
    text_3 = models.TextField(max_length=500,null=True)  
    text_4 = models.TextField(max_length=500,null=True)  
    text_5 = models.TextField(max_length=500,null=True)  

    staj = models.CharField(max_length=100)
    yash = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    rejm = models.TextField(max_length=250)
    muqavile = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.sirket
    def get_absolute_url(self):
        return f'/'
    
class Satish(models.Model):
    sirket = models.CharField(max_length=100)
    maas = models.CharField(max_length=50)
    seher = models.CharField(max_length=50)
    mezmun = models.CharField(max_length=200)    
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    text1 = models.TextField(max_length=500,null=True) 
    text2 = models.TextField(max_length=500,null=True)  
    text3 = models.TextField(max_length=500,null=True)  
    text4 = models.TextField(max_length=500,null=True)  
    text5 = models.TextField(max_length=500,null=True) 
    text_1 = models.TextField(max_length=500,null=True) 
    text_2 = models.TextField(max_length=500,null=True)  
    text_3 = models.TextField(max_length=500,null=True)  
    text_4 = models.TextField(max_length=500,null=True)  
    text_5 = models.TextField(max_length=500,null=True)  

    staj = models.CharField(max_length=100)
    yash = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    rejm = models.TextField(max_length=250)
    muqavile = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.sirket
    def get_absolute_url(self):
        return f'/'
    
class Techizat(models.Model):
    sirket = models.CharField(max_length=100)
    maas = models.CharField(max_length=50)
    seher = models.CharField(max_length=50)
    mezmun = models.CharField(max_length=200)    
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    text1 = models.TextField(max_length=500,null=True) 
    text2 = models.TextField(max_length=500,null=True)  
    text3 = models.TextField(max_length=500,null=True)  
    text4 = models.TextField(max_length=500,null=True)  
    text5 = models.TextField(max_length=500,null=True) 
    text_1 = models.TextField(max_length=500,null=True) 
    text_2 = models.TextField(max_length=500,null=True)  
    text_3 = models.TextField(max_length=500,null=True)  
    text_4 = models.TextField(max_length=500,null=True)  
    text_5 = models.TextField(max_length=500,null=True)  

    staj = models.CharField(max_length=100)
    yash = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    rejm = models.TextField(max_length=250)
    muqavile = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.sirket
    def get_absolute_url(self):
        return f'/'
    
class Marketinq(models.Model):
    sirket = models.CharField(max_length=100)
    maas = models.CharField(max_length=50)
    seher = models.CharField(max_length=50)
    mezmun = models.CharField(max_length=200)    
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    text1 = models.TextField(max_length=500,null=True) 
    text2 = models.TextField(max_length=500,null=True)  
    text3 = models.TextField(max_length=500,null=True)  
    text4 = models.TextField(max_length=500,null=True)  
    text5 = models.TextField(max_length=500,null=True) 
    text_1 = models.TextField(max_length=500,null=True) 
    text_2 = models.TextField(max_length=500,null=True)  
    text_3 = models.TextField(max_length=500,null=True)  
    text_4 = models.TextField(max_length=500,null=True)  
    text_5 = models.TextField(max_length=500,null=True)  

    staj = models.CharField(max_length=100)
    yash = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    rejm = models.TextField(max_length=250)
    muqavile = models.CharField(max_length=100)
    apply_link = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.sirket
    def get_absolute_url(self):
        return f'/'
    

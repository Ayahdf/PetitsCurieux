from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from prof.models import Enseignant
# Create your models here.

class tag(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom




class categorie(models.Model):
    nom = models.CharField( max_length=50)
    cover = models.ImageField( upload_to='categoryCovers/img/%y/',null=True)
    def __str__(self):
        return self.nom
    
class course(models.Model):
    titre = models.CharField(max_length=80)
    description = models.TextField()
    categorie = models.OneToOneField(categorie, null=True, on_delete=models.CASCADE)
    datecreation  = models.DateTimeField(auto_now=True)
    avis = models.IntegerField(null=True,validators=[MinValueValidator(0),MaxValueValidator(5)])
    cover = models.ImageField( upload_to='CourseCovers/img/%y/',null=True)
    video = models.FileField( upload_to='CourseVideos/lecons/%y',null=True)
    duration = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    tag = models.ManyToManyField(tag)
    Enseignant = models.ForeignKey(Enseignant, null=True, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    def __str__(self):
        return self.titre
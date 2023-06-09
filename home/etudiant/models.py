from django.db import models
from django.contrib.auth.models import User
from courses.models import course
# Create your models here.

class etudiant(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    nom = models.CharField(max_length=30)
    datenaissence = models.DateField(blank=True)
    photo = models.ImageField(upload_to='etudiant/img/pdp/%y',default='etudiant/img/pdp/23/def.png')
    levels = (
        ('1er annee','1er annee'),('2eme annee','2eme annee'),
        ('3eme annee','3eme annee'),('4eme annee','4eme annee'),
        ('5eme annee','5eme annee'),('6eme annee','6eme annee'),
    )
    NiveauEtudiant = models.CharField(max_length=50,choices=levels,blank=True)
    bio = models.TextField(null=True,blank=True,default="Etudiant On GoStudy E-learning")
    datecreation = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(course,null=True,on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.nom
    

class Enrollement(models.Model):
    cours = models.ForeignKey(course, null=True, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(etudiant, null=True, on_delete=models.CASCADE)
    datecreation = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cours.titre
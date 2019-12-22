from django.db import models
from model_utils import Choices

# Create your models here.

MODEL_CHOICES = (
    ('audi', 'Audi'),
    ('honda', 'Honda'),
    ('toyota', 'Toyota'),
)
TYP_CHOICES = Choices("benz", "diesel", "electric")

class Engine(models.Model):
    pojemnosc = models.IntegerField(blank=True, null=True) ## nie jest wymagane
    moc = models.IntegerField()
    typ = models.CharField(max_length=20, choices=TYP_CHOICES)
    name = models.CharField(max_length=255)

class Car(models.Model):
    model = models.CharField(max_length=20, choices=MODEL_CHOICES)
    rok_produkcji = models.IntegerField()
    marka = models.CharField(max_length=50)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)

    def __str__(self):
        return f"Car {self.model} | {self.marka} | {self.engine} | {self.rok_produkcji}"
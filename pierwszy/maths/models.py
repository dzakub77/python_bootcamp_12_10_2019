from django.db import models

# Create your models here.

OPERATION_CHOICES = (
    ("add", "Add"),
    ("sub", "Sub"),
    ("mul", "Mul"),
    ("div", "Div")
)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Math(models.Model):
    operation = models.CharField(max_length=10, choices=OPERATION_CHOICES) # w bazie to bedzie varchar
    a = models.IntegerField()
    b = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    resault = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Math {self.operation} | {self.a} | {self.b}"



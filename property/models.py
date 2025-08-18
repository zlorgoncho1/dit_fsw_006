from django.db import models

# Create your models here.
class Property(models.Model):
    """
    Schema de la table Property
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    description TEXT,
    price DECIMAL(10, 2),
    image VARCHAR(255),
    surface INT,
    rooms INT,
    bathrooms INT,
    garage BOOLEAN,
    garden BOOLEAN,
    city VARCHAR(100)
    """
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.TextField()
    surface = models.IntegerField()
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    city = models.CharField(max_length=100)

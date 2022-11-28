from django.db import models

# Create your models here.
class Order(models.Model):
    #size constants
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]
    #temp constants
    HOT = 'Hot'
    ICED = 'Iced'
    TEMP_CHOICES = [
        (HOT,'Hot'),
        (ICED,'Iced'),
    ]
    #flavor constants
    CARAMEL = 'Caramel'
    MOCHA = 'Mocha'
    FRENCH_VANILLA = 'French Vanilla'
    NO_FLAVOR = 'N/A'
    FLAVOR_CHOICES = [
        (CARAMEL,'Caramel'),
        (MOCHA,'Mocha'),
        (FRENCH_VANILLA,'French Vanilla'),
        (NO_FLAVOR,'None'),
    ]
    #dairy constants
    MILK = 'Milk'
    CREAM = 'Cream'
    ALMOND_MILK = 'Almond Milk'
    OAT_MILK = 'Oat Milk'
    NO_DAIRY = 'N/A'
    DAIRY_CHOICES = [
        (MILK,'Milk'),
        (CREAM,'Cream'),
        (ALMOND_MILK,'Almond Milk'),
        (OAT_MILK,'Oat Milk'),
        (NO_DAIRY,'None'),
    ]
    #sweetener constants
    SUGAR = 'Sugar'
    SPLENDA = 'Splenda'
    SWEET_N_LOW = "Sweet 'n Low"
    NO_SWEETENER = 'N/A'
    SWEETENER_CHOICES = [
        (SUGAR,'Sugar'),
        (SPLENDA,'Splenda'),
        (SWEET_N_LOW,"Sweet 'n Low"),
        (NO_SWEETENER,"None"),
    ]

    #Fields
    size = models.CharField(
        max_length = 15,
        choices = SIZE_CHOICES,
        default = MEDIUM,
    )
    temp = models.CharField(
        max_length = 15,
        choices = TEMP_CHOICES,
        default = HOT,
    )
    flavor = models.CharField(
        max_length = 20,
        choices = FLAVOR_CHOICES,
        default = NO_FLAVOR,
    )
    dairy = models.CharField(
        max_length = 20,
        choices = DAIRY_CHOICES,
        default = NO_DAIRY,
    )
    sweetener = models.CharField(
        max_length = 30,
        choices = SWEETENER_CHOICES,
        default = NO_SWEETENER,
    )
 
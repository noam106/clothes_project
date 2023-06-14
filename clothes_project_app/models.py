from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from clothes_project_app import validators

# Create your models here.

class Item(models.Model):

    CONDITION = {
        "condition":[
            ("as new", "As New"),
            ("used", "Used"),
            ("Needed repair", "needed_repair"),
            ("In box", "in_box"),
        ]
    }

    CLOTHES_LIST = {
        'clothe': [
            ('Sweater', 'sweater'),
            ('Jacket', "jacket"),
            ("Pants", "pants"),
            ("Vest", "vest"),
            ("Coat", "coat"),
            ("Dress", "dress"),
            ("Jeans", "jeans"),
            ("Shirt", "shirt"),
            ("Shorts", "shorts"),
            ("Swimsuit", "swimsuit"),
            ("Skirt", "skirt"),
            ("Sock", "sock"),
            ("Pajamas", "pajamas"),
            ("Cardigan", 'cardigan'),
            ("suit", "Suit"),
            ("Raincoat", "raincoat"),
            ("sleeveless_shirt", "Sleeveless shirt", "sleeveless shirt"),
            ("Belt", "belt"),
            ("other", "Other"),
        ]
    }

    class Meta:
        db_table = "items"
        ordering = ['id']

    item_type = models.CharField(max_length=256, choices=CLOTHES_LIST['clothe'], db_column= "item type")
    colors = models.CharField(max_length=128, db_column='colors', null=False, blank=False,)
    description = models.TextField(db_column='description', null=True, blank=True)
    condition = models.CharField(max_length=128, choices=CONDITION["condition"], db_column="item condition")

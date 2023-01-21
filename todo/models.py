from django.db import models
import uuid

# Create your models here.




class note(models.Model):
    uid = models.UUIDField(default=uuid.uuid4)
    titel = models.CharField('name', max_length=255)
    description = models.TextField('description', null=True, blank= True,)
    tags = models.ForeignKey("tags",  null=True, blank= True, on_delete=models.SET_NULL)
    
    
    
    
class TagsTypeChoices(models.TextChoices):
    WORK = "WORK", "Work"
    STUDY = "STUDY", "Study"
    INCOME = "INCOME", "Income"
    FAMILY = "FAMILY", "Family"
    
    
class tags(models.Model):
    type = models.CharField(max_length=255, choices=TagsTypeChoices.choices)
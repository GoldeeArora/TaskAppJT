from django.db                  import models
from django.contrib.auth.models import AbstractUser

#====================================================================
# Extending default User model to include mobile field
#====================================================================
class User(AbstractUser):
    mobile = models.CharField(max_length=15)

#====================================================================
# Task Model with many to many relation to User model
#====================================================================
class Task(models.Model):
    #----------------------------------------------------------------
    # Choices for status and task_type
    #----------------------------------------------------------------
    STATUS_CHOICES = (
        ("ACTIVE"    , "ACTIVE"    ),
        ("COMPLETE"  , "COMPLETE"  ),
        ("INCOMPLETE", "INCOMPLETE"),
    )

    TASK_TYPE_CHOICES = (
        ("HIGH_PRIORITY", "HIGH_PRIORITY"),
        ("NORMAL"       , "NORMAL"       ),
        ("LOW_PRIORITY" , "LOW_PRIORITY" ),
    )

    #----------------------------------------------------------------
    # Foreign Relations: User (Many to Many)
    #----------------------------------------------------------------
    user = models.ManyToManyField(User)

    #----------------------------------------------------------------
    # Domestic fields: completed_at is null while task is incomplete
    #----------------------------------------------------------------
    name         = models.CharField(max_length=64)
    description  = models.CharField(max_length=1024)
    task_type    = models.CharField(max_length=64, choices=TASK_TYPE_CHOICES, default="NORMAL")
    status       = models.CharField(max_length=64, choices=STATUS_CHOICES   , default="ACTIVE")
    created_at   = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import	receiver

ROLE_CHOICE = (
	(1, 'Admin'),
	(2, 'Gestor'),
	(3, 'Aprendiz')
)


from .Department import Department
from .Course import Course
from .Profile import Profile
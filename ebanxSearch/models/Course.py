from ebanxSearch.models import *

class Course(models.Model):
    name = models.CharField(null=False,	max_length=255)	
    description = models.TextField(null=False,max_length=255)
    url = models.CharField(null=False,max_length=255)
    workload = models.IntegerField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    
    def	__str__(self):
        return '{}'.format(self.name)


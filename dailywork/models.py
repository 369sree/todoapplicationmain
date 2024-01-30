from django.db import models

class Work(models.Model):
    user=models.CharField(max_length=100)
    task=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True,blank=True)
    note=models.CharField(max_length=100)
    options=(
        ("completed","completed"),
        ("pending","pending")
    )
    status=models.CharField(max_length=20,choices=options,default="pending")

    
    
    def __str__(self):
        return self.task
    



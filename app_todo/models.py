from django.db import models

# Create your models here.
class UserDetails(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150, null=True)
    contact = models.IntegerField()
    is_verified = models.BooleanField(null=True, blank=True)

    def __str__(self):
         return self.first_name
    
    class Meta:
        db_table = "User_Details"

class UserTodo(models.Model):
    todo = models.CharField(max_length=200)
    desc = models.CharField(max_length=250)
    expired_date = models.DateField()
    is_completed = models.BooleanField()
    usertodo = models.ForeignKey(UserDetails, on_delete = models.CASCADE)
    
    # def __str__(self):
    #     return self.todo

    class Meta:
        db_table = "UserTodo"
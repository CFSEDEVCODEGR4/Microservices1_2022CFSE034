from django.db import models
from django.urls import reverse

# ===============================================================
# User Model
# ===============================================================
class User(models.Model):    
    user_id = models.CharField(max_length = 15)                                          #Example: UID001
    user_name = models.CharField(max_length = 40,)                                     
    user_email = models.CharField(max_length = 40,)     
    user_mobile = models.CharField(max_length = 10,) 
    user_password = models.CharField(max_length = 40,)  
                                                                        
    user_role = models.CharField(max_length = 1,blank=False,default=1)     

    class Meta:
        ordering = ['user_id']

    def get_absolute_url(self):
        return reverse('user_id', args=[str(self.id)])   
        
    def __str__(self):
        return self.user_id
# ===============================================================








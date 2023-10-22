# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.contrib.auth.hashers import make_password, check_password



class Users(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    userpassword = models.CharField(max_length=255, blank=True, null=True)

    def set_password(self, raw_password):
        self.userpassword = make_password(raw_password)

    def verify_password(self, raw_password):
        return check_password(raw_password, self.userpassword)

    class Meta:
        managed = False
        db_table = 'users'


    

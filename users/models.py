from django.db import models
from django.contrib.auth.models import User

class Universities(models.Model):
    unitid = models.IntegerField(db_column='UnitID', primary_key=True)  # Field name made lowercase.
    institution = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    size_category = models.IntegerField(blank=True, null=True)
    urbanization = models.IntegerField(blank=True, null=True)
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    website = models.TextField(blank=True, null=True)
    region = models.IntegerField(blank=True, null=True)
    admission_rate = models.TextField(blank=True, null=True)
    admission_yield = models.TextField(blank=True, null=True)
    finaid_rate = models.TextField(blank=True, null=True)
    tuition_instate = models.TextField(blank=True, null=True)
    tuition_outstate = models.TextField(blank=True, null=True)
    totalstudents = models.IntegerField(blank=True, null=True)
    total_women = models.IntegerField(blank=True, null=True)
    total_asian = models.IntegerField(blank=True, null=True)
    total_black = models.IntegerField(blank=True, null=True)
    total_hispanic = models.IntegerField(blank=True, null=True)
    total_pacific = models.IntegerField(blank=True, null=True)
    student_faculty_ratio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universities'

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    firstname = models.CharField(max_length=50, verbose_name="First Name:")
    lastname = models.CharField(max_length=50, verbose_name="Last Name:")
    description = models.TextField(default="This user has not provided an about me.")
    image = models.TextField(default="http://via.placeholder.com/150")



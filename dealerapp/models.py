from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Anumandal(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Block(models.Model):
    anumandal = models.ForeignKey(Anumandal, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Panchayat(models.Model):
    name = models.CharField(max_length=50)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    vaccant = models.CharField(max_length=5, default = "0")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Dealer(models.Model):
    anumandal = models.ForeignKey(Anumandal, on_delete=models.SET_NULL, null=True)
    block = models.ForeignKey(Block, on_delete=models.SET_NULL, null=True)
    panchayat = models.ForeignKey(Panchayat, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=100, blank=False, null=False)
    husband_father_name = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(max_length=100, blank=False, null=False)
    gender = models.CharField(max_length=100, blank=False, null=False)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    qualication = models.CharField(max_length=100, blank=False, null=False)
    mobile_number = models.PositiveIntegerField(unique = True)
    email = models.EmailField()
    aadhar_number = models.PositiveIntegerField(unique = True)
    img = models.ImageField(upload_to="images", blank=True)
    currentaddress = models.CharField(max_length=256, blank=True, null=True)
    permanentaddress = models.CharField(max_length=256, blank=True, null=True)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    holding_no = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    khata_no = models.CharField(max_length=100, blank=True, null=True)
    khesra_no = models.CharField(max_length=100, blank=True, null=True)
    ward_no = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    thana = models.CharField(max_length=100, blank=True, null=True)
    zila = models.CharField(max_length=100, blank=True, null=True)
    computer_file =models.FileField(upload_to="computer", blank=True)
    aadhar_file =models.FileField(upload_to="aadhar", blank=True)
    matric_file =models.FileField(upload_to="matric", blank=True)
    inter_file =models.FileField(upload_to="inter", blank=True)
    graduation_file =models.FileField(upload_to="graduation", blank=True)
    post_graduation_file =models.FileField(upload_to="postgraduate", blank=True)
    caste_file =models.FileField(upload_to="caste", blank=True)
    residence_file =models.FileField(upload_to="residence", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.full_name

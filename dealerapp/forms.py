from unicodedata import category
from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Transgender', 'Transgender')
]

CATEGORY_CHOICES = [
    ('GENERAL', 'GENERAL'),
    ('OBC', 'OBC'),
    ('SC', 'SC'),
    ('ST', 'ST'),
    ('EWS', 'EWS'),
]



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']


class DealerForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Dealer
        fields = '__all__'
        labels = {'anumandal': 'Select Your Anumandal', 'block': 'Select Your Block', 'panchayat': 'Select Your Panchayat',
                  'full': 'Enter Your Full Name', 'husband_father_name': 'Enter Your Husband/Father Name',
                   'dob': 'Date of Birth', 'qualication': 'Enter Your Highest Qualification',
                   'mobile_number': 'Enter Your Mobile No.', 'email': 'Enter Your Email.','email': 'Enter Your Email.','aadhar_number': 'Enter Your Aadhar No.',
                  'img': 'Upload your Image', 'currentaddress': 'Enter Your Coreesepondence Address.','permanentaddress': 'Enter Your Permanent Address.',
                  'house_no': 'Enter Your House/Shop No.', 'holding_no': 'Enter Your Holding No.','area': 'Enter Your Area/Kshetraphal',
                  'khata_no': 'Enter Your Khata No.', 'khesra_no': 'Enter Your Khesra No.','ward_no': 'Enter Your Ward No.',
                  'city': 'Enter Your City Name.', 'thana': 'Enter Your Thana.','zila': 'Enter Your Zila',
                   'computer_file': 'Upload Computer Certificate','aadhar_file': 'Upload Your Aadhar',
                  'matric_file': 'Upload Your Matric Certificate',
                  'inter_file': 'Upload Your Intermediate Certificate', 'graduate_file': 'Upload Your Graduation Certificate',
                  'post_graduation_file': 'Upload Your Post Graduate Certificate',
                  'caste_file': 'Upload Your Caste Certificate.', 'residence_file': 'Upload Your Residence Certificate.',

                  }
        #fields = ('name', 'birthdate', 'country', 'city', 'vanue')
        widgets = {
            'anumandal': forms.Select(attrs={'class': 'form-select'}),
            'block': forms.Select(attrs={'class': 'form-select'}),
            'panchayat': forms.Select(attrs={'class': 'form-select'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'husband_father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-selcet'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'qualication': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
            'currentaddress': forms.TextInput(attrs={'class': 'form-control'}),
            'permanentaddress': forms.TextInput(attrs={'class': 'form-control'}),
            'house_no': forms.TextInput(attrs={'class': 'form-control'}),
            'holding_no': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'khata_no': forms.TextInput(attrs={'class': 'form-control'}),
            'khesra_no': forms.TextInput(attrs={'class': 'form-control'}),
            'ward_no': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'thana': forms.TextInput(attrs={'class': 'form-control'}),
            'zila': forms.TextInput(attrs={'class': 'form-control'}),


        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['block'].queryset = Block.objects.none()

        if 'anumandal' in self.data:
            try:
                anumandal_id = int(self.data.get('anumandal'))
                self.fields['block'].queryset = Block.objects.filter(
                    anumandal_id=anumandal_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['block'].queryset = self.instance.anumandal.block_set.order_by(
                'name')

        self.fields['panchayat'].queryset = Block.objects.none()
        if 'block' in self.data:
            try:
                block_id = int(self.data.get('block'))
                self.fields['panchayat'].queryset = Panchayat.objects.filter(
                    block_id=block_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            #self.fields['vanue'].queryset = self.instance.country.city.vanue_set.order_by('name')
            self.fields['panchayat'].queryset = self.instance.block.panchayat_set.order_by(
                'name')

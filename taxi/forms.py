from django import forms
from .models import Driver, Car


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = (self.cleaned_data.
                          get("license_number"))
        if len(license_number) != 8:
            raise (forms.ValidationError
                   ("license number must be 8 characters long!"))
        if (not license_number[0:3].isalpha()
                or license_number[0:3] != license_number[0:3].upper()):
            raise (forms.ValidationError
                   ("license number 3 first letters must be uppercase"))

        if not license_number[3:].isnumeric():
            raise (forms.ValidationError
                   ("license number last 5 letters must be numbers"))
        return license_number


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("drivers", "manufacturer", "model")
        widgets = {
            "drivers" : forms.CheckboxSelectMultiple()
        }

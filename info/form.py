from django import forms
from .models import Project

class addProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'text']






# class AddInfoCatModelForm(forms.ModelForm):
#     class Meta:
#         model = InfoCat
#         field = ["name"]
#         widgets = {
#             "name": forms.TextInput(attrs={})
#         }

# class AddInfoSubCatModelForm(forms.ModelForm):
#     class Meta:
#         model = InfoSubCat(forms.ModelForm)
#         fields = ["name", "category"]
#         widgets = {
#             "name": forms.TextInput(attrs={})
#         }

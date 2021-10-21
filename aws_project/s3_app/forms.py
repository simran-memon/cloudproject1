from django import forms

from .models import s3Object


class ObjectForm(forms.ModelForm):
    class Meta:
        model = s3Object
        fields = ('description', 's3_storage_object')
        #fields = "__all__"

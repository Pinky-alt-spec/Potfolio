from django import forms

class contactEmail(forms.Form):
    contact_name=forms.CharField(required=True)
    contact_email=forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    contact_message=forms.CharField(widget=forms.Textarea,required=True)






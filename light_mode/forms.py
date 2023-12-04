from django import forms
from captcha.fields import CaptchaField
from light_mode.models import Contact, NewsLetter

class ContactForm(forms.ModelForm):
    captcha = CaptchaField(label='Please enter the characters in the image')
    class Meta:
        model = Contact
        fields = "__all__"

class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = "__all__"
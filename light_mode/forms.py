from django import forms
from captcha.fields import CaptchaField
from light_mode.models import Contact, NewsLetter

class ContactForm(forms.ModelForm):
    captcha = CaptchaField(label='متن زیر را وارد کنید')
    class Meta:
        model = Contact
        fields = "__all__"

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = "__all__"
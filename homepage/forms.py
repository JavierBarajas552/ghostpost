from django import forms
from homepage.models import PostModle


class PostForm(forms.Form):
    body = forms.CharField(max_length=280)
    post_type = forms.ChoiceField(choices=(("1", "Boast"), ("2", "Roast")))

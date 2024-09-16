from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from .models import *

class PostCreateForm(forms.ModelForm):

    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
    helper.add_input(
        Button(
            "cancel",
            "Cancel",
            css_class="btn",
            onclick=f"javascript:location.href = '/posts/';",
        )
    )
    helper.form_method = "POST"

    class Meta:
        model = Post
        fields = '__all__'

class CommentCreateForm(forms.ModelForm):

    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
    helper.add_input(
        Button(
            "cancel",
            "Cancel",
            css_class="btn",
            onclick=f"javascript:location.href = '/posts/';",
        )
    )
    helper.form_method = "POST"

    class Meta:
        model = Comment
        fields = '__all__'
        
class TagCreateForm(forms.ModelForm):

    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
    helper.add_input(
        Button(
            "cancel",
            "Cancel",
            css_class="btn",
            onclick=f"javascript:location.href = '/posts/';",
        )
    )
    helper.form_method = "POST"

    class Meta:
        model = Tag
        fields = '__all__'
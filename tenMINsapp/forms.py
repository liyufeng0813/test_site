from django import forms
from django.core.exceptions import ValidationError

def name_validators(username):
    if len(username) < 1:
        raise ValidationError("Not enough words")

def length_validator(password):
    if len(password) < 8:
        raise ValidationError('Not enough words,at least eight')

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=15,
        validators=[name_validators]
    )
    password = forms.CharField(
        validators=[length_validator]
    )

def words_validator(comment):
    if len(comment) < 3:
        raise ValidationError('Not enough words')

def comment_validator(comment):
    # if 'fuck' in comment:
    #     raise ValidationError('Do not use "fuck" ')
    Keywords = ['发票','钱','father','mother','fuck']
    for Keyword in Keywords:
        if Keyword in comment:
            raise ValidationError('Do not use ：‘发票’,‘钱’,‘father‘,’mother‘,’fuck‘ ')

def namewords_validator(name):
    if 'xx' in name:
        raise ValidationError("Do not use ：‘xx’")


class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        validators=[namewords_validator]
    )
    content = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'required':'Such words'
        },
        validators=[words_validator,comment_validator]
    )


def name_length_validator(姓名):
    if len(姓名) > 15 :
        raise ValidationError("max_length: 15.")

def password_length_validator(密码):
    if len(密码) > 15 :
        raise ValidationError("max_length: 15.")

class MyinfoForm(forms.Form):
    name = forms.CharField(
        max_length=15,
        validators=[name_length_validator]
    )
    sex = forms.ChoiceField(
        choices=(
            ('保密', '保密'),
            ('男', '男'),
            ('女', '女'),
        )
    )
    password = forms.CharField(
        max_length=15,
        validators=[password_length_validator]
    )
    image = forms.FileField(max_length=300, allow_empty_file=True)
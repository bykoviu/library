from .models import Comment
from django.forms import ModelForm, TextInput, CharField, PasswordInput, ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'comm']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'comm': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add your comment'
            })
        }

class AuthUserForm(AuthenticationForm, ModelForm):
    password = CharField(widget=PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Enter your nickname'
        self.fields['password'].label = 'Enter your password'
    
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise ValidationError(f'Пользователь {username} не зарегистрирован.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise ValidationError('Не верный пароль')
        return self.cleaned_data
    
    class Meta:
        model = User
        fields = ['username', 'password']
    

class RegisterUserForm(ModelForm):
    password = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Repeat password', widget=PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    
    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # for field in self.fields:
            # self.fields[field].widget.attrs['class'] = 'form-control'
    # def save(self, commit=True):
        # user = super().save(commit=False)
        # user.set_password(self.cleaned_data['password'])
        # if commit:
            # user.save()
        # return user
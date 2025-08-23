from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from tasks.models import Task
class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

class AddTask(ModelForm):
    class Meta:
        model = Task
        fields = ('name','description',)
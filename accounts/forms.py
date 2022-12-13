from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username", 
            "email", 
            "image",
            ) 



class ChangeUserForm(UserChangeForm):
        password = None

        class Meta:
            model = get_user_model()
            fields = (
                "username", 
                "image", 
                "email",
                )
from django import forms
from .models import Competition, Participate, Profile


# class TitleField(forms.Field):
#     def validate(self, value):
#         super(TitleField, self).validate(value)
#         if not self.pk and self.title and TitleField.objects.filter(title=self.title).exists():
#             raise forms.ValidationError("Объект с таким именем уже существует")


class CompetitionForm(forms.ModelForm, forms.Field):
    class Meta:
        model = Competition
        fields = ('title', 'comp_type', 'rules', 'short_description', 'expiry_date', 'survey_date')


class ParticipateForm(forms.ModelForm):
    class Meta:
        model = Participate
        fields = ('title', 'comment', 'content')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'location', 'birth_date')


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Имя пользователя',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Пароль',
        max_length=32,
        widget=forms.PasswordInput()
    )

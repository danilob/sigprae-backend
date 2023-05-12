from django import forms
from usersystem.models import User

from django.core.exceptions import ValidationError

from datetime import datetime

from validate_docbr import CPF

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username",'password', "email",'full_name','cpf','genre','birth_date','profile','phone_number']

    password=forms.CharField(label="Senha",widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    def clean_confirm_password(self):
        data_password = self.cleaned_data['password']
        data_confirm_password = self.cleaned_data['confirm_password']
        if not data_password == data_confirm_password:
            raise ValidationError("Confirmação de senha não confere.")

        return data_confirm_password

    def clean_birth_date(self):
        data_birth_date = self.cleaned_data['birth_date']
        data_today = datetime.today().strftime("%Y-%m-%d")
        if not (User.validate_age(data_birth_date.strftime("%Y-%m-%d"),data_today)):
            raise ValidationError("Você não é maior de idade.")

        return data_birth_date




#Referência útil
#https://docs.djangoproject.com/en/4.0/ref/forms/fields/
class UserEssentialForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password",'profile',"email",'full_name','cpf','birth_date']
        help_texts = {
            'birth_date' : 'Formato: dd/mm/aaaa',
        }
        labels = {
            "profile": "Perfil",
            "cpf": "CPF",
            "full_name": "Nome completo",
            "birth_date": "Data de nascimento"
        }
        widgets = {
            'cpf': forms.TextInput(attrs={'class':'form-control'}),
        } 
    password=forms.CharField(label="Senha",widget=forms.PasswordInput())
    confirm_password=forms.CharField(label="Confirme sua Senha",widget=forms.PasswordInput())

    terms_and_conditions = forms.BooleanField(label="Aceita os termos?",required=False)


    def __init__(self, *args, **kwargs):
        super(UserEssentialForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu E-mail'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Digite seu Nome Completo'
        self.fields['cpf'].widget.attrs['placeholder'] = 'Digite seu CPF'
        self.fields['birth_date'].widget.attrs['placeholder'] = 'Data de Nascimento'
        self.fields['password'].widget.attrs['placeholder'] = 'Digite a Senha'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirme a Senha'
        

   
    # - verificar confirmação de senha
    def clean_confirm_password(self):
        data_password = self.cleaned_data['password']
        data_confirm_password = self.cleaned_data['confirm_password']
        if not data_password == data_confirm_password:
            raise ValidationError("Confirmação de senha não confere.")

        return data_confirm_password
    
    # - verificar maior de idade
    def clean_birth_date(self):
        data_birth_date = self.cleaned_data['birth_date']
        if not data_birth_date:
            raise ValidationError("Você não inseriu sua data de nascimento.")
        data_today = datetime.today().strftime("%Y-%m-%d")
        if not (User.validate_age(data_birth_date.strftime("%Y-%m-%d"),data_today)):
            raise ValidationError("Você não é maior de idade.")

        return data_birth_date

    # - verificar email e profile
    def clean_email(self):
        data_email = self.cleaned_data['email']
        data_profile = self.cleaned_data['profile']
        if (data_profile == User.USER_PROFESSOR) and (not User.check_professor_email(data_email)): 
            raise ValidationError("Não foi colocado e-mail de Professor Institucional.")
        elif (data_profile == User.USER_STUDENT) and (not User.check_student_email(data_email)):
            raise ValidationError("Não foi colocado e-mail de Aluno Institucional.")
        elif (data_profile == User.USER_COMMUNITY):
            if User.check_professor_email(data_email):
                raise ValidationError("Você inseriu um e-mail de Professor Institucional.")
            elif User.check_student_email(data_email):
                raise ValidationError("Você inseriu um e-mail de Estudante Institucional.")
            elif User.check_worker_email(data_email):
                raise ValidationError("Você inseriu um e-mail de Técnico Administrativo Institucional.")
        if (data_profile == User.USER_WORKER) and (not User.check_worker_email(data_email)):
            raise ValidationError("Não foi colocado e-mail de Técnico Administrativo Institucional.")

        return data_email
        

    def clean_cpf(self):
        data_cpf = self.cleaned_data['cpf']
        if not data_cpf:
            raise ValidationError("Você não inseriu o CPF.")
        cpf = CPF()
        if not cpf.validate(data_cpf):
            raise ValidationError("Você inseriu um CPF inválido.")
        
        if User.objects.filter(cpf=data_cpf).exists():
            raise ValidationError("Um usuário com este CPF já está cadastrado.")

        return data_cpf

    # - verificar se marcou o termo de consentimento
    def clean_terms_and_conditions(self):
        data_terms = self.cleaned_data['terms_and_conditions']
        if not data_terms:
            raise ValidationError("Você precisa concordar com os Termos e Condições.")

        return data_terms
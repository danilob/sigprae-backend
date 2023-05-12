from django.test import TestCase

from usersystem.forms import UserForm

from usersystem.forms import UserEssentialForm

from usersystem.models import User

from validate_docbr import CPF

class UserFormTest(TestCase):

    def test_user_form_valid(self):
        form = UserForm(data={
            'username': 'user',
            'email': 'user@novaera.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '2000-02-01',
            'phone_number' : '0012',
            'profile' : User.USER_COMMUNITY,
            'genre' : User.GENRE_MALE,
            'cpf':CPF().generate(),
        })
        #print(form)
        #print(form.data['cpf'],CPF().validate(form.data['cpf']))
        #print(form.errors)
        self.assertTrue(form.is_valid())

    def test_user_form_invalid(self):
        form = UserForm(data={
            'username': 'user',
            'email': 'user@novaera.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '2010-02-01',
            'phone_number' : '0012',
            'profile' : User.USER_COMMUNITY,
            'genre' : User.GENRE_MALE,
            'cpf':CPF().generate(),
        })

        self.assertFalse(form.is_valid())


class UserEssentialFormTest(TestCase):

    def test_user_essential_form_valid(self):
        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'user@novaera.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '2000-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })

        self.assertTrue(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'rubens@prp.uespi.br',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_PROFESSOR,
            'cpf':CPF().generate(),
        })

        self.assertTrue(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'rubens@aluno.uespi.br',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
             'terms_and_conditions': True,
            'profile' : User.USER_STUDENT,
            'cpf':CPF().generate(),
        })

        self.assertTrue(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'rubens@gmail.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })

        self.assertTrue(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'rubens@gmail.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })

        self.assertTrue(form.is_valid())

        #Teste USER_WORKER
        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'user@uespi.br',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '2000-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_WORKER,
            'cpf':CPF().generate(),
        })

        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_user_essential_form_invalid_fiels(self):
        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'user@novaera.com',
            'password': 'password', 
            'confirm_password': 'password123',
            'full_name': 'Pedro',
            'birth_date' : '2010-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
        })

        self.assertFalse(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'user@novaera.com',
            'password': 'password', 
            'confirm_password': 'password123',
            'full_name': 'Pedro',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })

        self.assertFalse(form.is_valid())

        cpf = CPF().generate()
        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'user@novaera.com',
            'password': 'password123', 
            'confirm_password': 'password123',
            'full_name': 'Pedro',
            'birth_date' : '2000-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':cpf,
        })
        form.save()

        form = UserEssentialForm(data={
            'username': 'user123',
            'email': 'user2@novaera.com',
            'password': 'password123', 
            'confirm_password': 'password123',
            'full_name': 'Pedro',
            'birth_date' : '2000-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':cpf,
        })
        self.assertFalse(form.is_valid())

    def test_user_essential_form_invalid(self):
        #testando password inválido
        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'user@novaera.com',
            'password': 'password', 
            'confirm_password': 'password123',
            'full_name': 'Pedro',
            'birth_date' : '2010-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })

        self.assertFalse(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'user@novaera.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '2010-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })


        self.assertFalse(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'user@novaera.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_PROFESSOR,
            'cpf':CPF().generate(),
        })
        
        self.assertFalse(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'rubens@prp.uespi.br',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_STUDENT,
            'cpf':CPF().generate(),
        })

        self.assertFalse(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'rubens@phb.uespi.br',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })

        self.assertFalse(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'rubens@aluno.uespi.br',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })

        self.assertFalse(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'rubens@uespi.br',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })

        self.assertFalse(form.is_valid())

        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'alguem@gmail.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_COMMUNITY,
            'cpf':'012.912.830-43',
        })

        self.assertFalse(form.is_valid())

        #Teste USER_WORKER
        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'user@gmail.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '2000-02-01',
            'terms_and_conditions': True,
            'profile' : User.USER_WORKER,
            'cpf':CPF().generate(),
        })

        self.assertFalse(form.is_valid())

        #verificar um formulario inválido devido ao termo de consentimento não marcado
        form = UserEssentialForm(data={
            'username': 'user',
            'email': 'alguem@gmail.com',
            'password': 'password', 
            'confirm_password': 'password',
            'full_name': 'Pedro',
            'birth_date' : '1980-02-01',
            'terms_and_conditions': False,
            'profile' : User.USER_COMMUNITY,
            'cpf':CPF().generate(),
        })

        
        self.assertFalse(form.is_valid())
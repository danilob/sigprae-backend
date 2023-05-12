from unicodedata import category
from django.db import models

from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    USER_PROFESSOR = 'UP'
    USER_WORKER = 'UW'
    USER_STUDENT = 'US'
    USER_COMMUNITY = 'UC'
    #Professor, Student, Worker, Administrator, Community
    USER_PROFILE = (
        (USER_PROFESSOR,'Professor'),
        (USER_WORKER,'Técnico Administrativo'),
        (USER_STUDENT,'Estudante'),
        (USER_COMMUNITY,'Membro da Comunidade')
    )

    GENRE_MALE = 'M'
    GENRE_FEMALE = 'F'
    GENRE_NULL = 'O'

    USER_GENRE = (
        (GENRE_MALE,'Masculino'),
        (GENRE_FEMALE,'Feminino'),
        (GENRE_NULL,'Não Informado')
    )

    full_name = models.CharField(max_length=100, blank=True,null=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, blank=True,null=True) #86999494681

    profile = models.CharField('Perfil', max_length=2,choices=USER_PROFILE,blank=True,null=True)
    genre = models.CharField('Gênero', max_length=1,choices=USER_GENRE,default=GENRE_NULL)
    cpf  = models.CharField(max_length=11, blank=True,null=True)
    slug = models.SlugField(max_length=150,unique=True,default="page-slug")

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-full_name']

    def __str__(self):
        return self.full_name if (self.full_name) else self.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()
        super(User, self).save(*args, **kwargs)

    @property
    def has_active_term(self):
        return self.userterms.all().exists()

    @property
    def get_active_term(self):
        if(self.has_active_term):
            return self.userterms.all().last().terms
        return None


    @staticmethod
    def validate_age(birth_date,today_date):
        '''
            brith_date e today_date tem o formado AAAA-MM-DD
        '''
        from datetime import datetime
        #https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        new_birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        new_today_date = datetime.strptime(today_date, '%Y-%m-%d')
        diff = new_today_date - new_birth_date
        years = diff.days // 365
        if(years >= 18):
            return True
        else:
            return False

    @staticmethod
    def register(username,birth,full_name,password):
        if(len(username) < 5):
            return False
        if(len(birth)==10):
            import re
            expression = "^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
            match = re.search(expression, birth)
            if not match:
                return False
        else:
            return False

        if(len(full_name)<5):
            return False

        if not (len(password)>=8):
            return False
        
        if (User.objects.filter(username=username).exists()):
            return False

        User.objects.create(username=username, password=password,full_name=full_name,birth_date=birth)
        
        return True

    @staticmethod
    def check_student_email(email):
        import re
        match = re.search("@aluno\.uespi\.br", email)
        return True if (match) else False

    @staticmethod
    def check_professor_email(email):
        import re
        match = re.search("@[^(aluno)].*\.uespi\.br", email)
        return True if (match) else False

    @staticmethod
    def check_worker_email(email):
        import re
        match = re.search("@uespi\.br", email)
        return True if (match) else False
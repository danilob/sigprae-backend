from django.test import TestCase

from usersystem.models import User
from usersystem.tests.factory_for_testing import UserFactory

class TestUser(TestCase):

    def setUp(self):
        self.user1 = UserFactory.create_valid_instance(
            profile = User.USER_PROFESSOR,
            email = "danilo@frn.uespi.br"
        )

    def test_check_age_user(self):
        self.assertEquals(User.validate_age('1989-04-18','2022-02-08'),True)#AAAA-MM-DD
        self.assertEquals(User.validate_age('2012-04-18','2022-02-08'),False)#AAAA-MM-DD
        self.assertEquals(User.validate_age('2004-02-08','2022-02-08'),True)#AAAA-MM-DD

    def test_email_professor(self):
        self.assertEquals(User.check_professor_email("danilo@frn.uespi.br"),True)
        self.assertEquals(User.check_professor_email("rocha@phb.uespi.br"),True)
        self.assertEquals(User.check_professor_email("vigno@prp.uespi.br"),True)
        self.assertEquals(User.check_professor_email("teofilosantos@aluno.uespi.br"),False)
        self.assertEquals(User.check_professor_email("brunacbesilva@aluno.uespi.br"),False)
        self.assertEquals(User.check_professor_email("mmvieira@aluno.uespi.br"),False)
        self.assertEquals(User.check_professor_email("cavi@uespi.br"),False)
        self.assertEquals(User.check_professor_email(self.user1.email),True)

    def test_email_worker(self):
        self.assertEquals(User.check_worker_email("danilo@frn.uespi.br"),False)
        self.assertEquals(User.check_worker_email("rocha@phb.uespi.br"),False)
        self.assertEquals(User.check_worker_email("vigno@prp.uespi.br"),False)
        self.assertEquals(User.check_worker_email("teofilosantos@aluno.uespi.br"),False)
        self.assertEquals(User.check_worker_email("brunacbesilva@aluno.uespi.br"),False)
        self.assertEquals(User.check_worker_email("mmvieira@aluno.uespi.br"),False)
        self.assertEquals(User.check_worker_email("cavi@uespi.br"),True)

    def test_email_student(self):
        self.assertEquals(User.check_student_email("danilo@frn.uespi.br"),False)
        self.assertEquals(User.check_student_email("rocha@phb.uespi.br"),False)
        self.assertEquals(User.check_student_email("vigno@prp.uespi.br"),False)
        self.assertEquals(User.check_student_email("teofilosantos@aluno.uespi.br"),True)
        self.assertEquals(User.check_student_email("brunacbesilva@aluno.uespi.br"),True)
        self.assertEquals(User.check_student_email("mmvieira@aluno.uespi.br"),True)
        self.assertEquals(User.check_student_email("cavi@uespi.br"),False)

    def test_register_user(self):
        self.assertEquals(User.register(
            username = "dan",
            birth = "1989-04-18",
            full_name = "Danilo Borges da Silva",
            password = "12345678",
        ),False)
        self.assertEquals(User.register(
            username = "danilo",
            birth = "1989-04-18",
            full_name = "Danilo Borges da Silva",
            password = "",
        ),False)
        self.assertEquals(User.register(
            username = "danilo",
            birth = "",
            full_name = "Danilo Borges da Silva",
            password = "12345678",
        ),False)
        self.assertEquals(User.register(
            username = "danilo",
            birth = "1989-04-18",
            full_name = "Danilo Borges da Silva",
            password = "12345678",
        ),True)
        self.assertEquals(User.register(
            username = "danilo",
            birth = "1989-04-18",
            full_name = "",
            password = "12345678",
        ),False)
        self.assertEquals(User.register(
            username = "danilo",
            birth = "1989-04-18",
            full_name = "Danilo Borges da Silva",
            password = "12345678",
        ),False)
        self.assertEquals(User.register(
            username = "danilob",
            birth = "1989-04-18",
            full_name = "Danilo Borges da Silva",
            password = "12345678",
        ),True)

from django.utils import timezone
import pytz
from termsandconditions.models import UserTermsAndConditions, TermsAndConditions

class TestTermsAndConditionsUser(TestCase):
    def setUp(self):
        self.user1 = UserFactory.create_valid_instance(
            profile = User.USER_PROFESSOR,
            email = "danilo@frn.uespi.br"
        )
        #print(self.user1.full_name)
        self.term_and_condition = TermsAndConditions.objects.create(
            name = "Termo e Condição",
            date_active = timezone.now()
        )

        

    def test_user_has_accept_term_and_condition(self):
        self.assertEquals(self.user1.has_active_term,False)
        UserTermsAndConditions.objects.create(
            user = self.user1,
            terms = self.term_and_condition
        )
        self.assertEquals(self.user1.has_active_term,True)

    def test_user_get_accept_term_and_condition(self):
        UserTermsAndConditions.objects.create(
            user = self.user1,
            terms = self.term_and_condition
        )
        self.assertEqual(self.user1.get_active_term, self.term_and_condition)

        term_and_condition_2 = TermsAndConditions.objects.create(
            name = "Termo e Condição 2",
            date_active = timezone.now()
        )

        user_terms = UserTermsAndConditions.objects.create(
            user = self.user1,
            terms = term_and_condition_2
        )

        self.assertEqual(self.user1.get_active_term, term_and_condition_2)
        print(user_terms.ip_address)
        print(user_terms.date_accepted)


    def test_user_term_and_condition_access(self):
        UserTermsAndConditions.objects.create(
            user = self.user1,
            terms = self.term_and_condition
        )
        self.assertEquals(self.term_and_condition.users.all().count(),1)
        user2 = UserFactory.create_valid_instance(
            profile = User.USER_PROFESSOR,
            email = "alex@prp.uespi.br"
        )
        UserTermsAndConditions.objects.create(
            user = user2,
            terms = self.term_and_condition
        )
        self.assertEquals(self.term_and_condition.users.all().count(),2)


    def test_user_term_and_condition_user_list(self):
        UserTermsAndConditions.objects.create(
            user = self.user1,
            terms = self.term_and_condition
        )
        # self.assertEquals(self.term_and_condition.users.all().count(),1)
        user2 = UserFactory.create_valid_instance(
            profile = User.USER_PROFESSOR,
            email = "alex@prp.uespi.br"
        )
        UserTermsAndConditions.objects.create(
            user = user2,
            terms = self.term_and_condition
        )
        # self.assertEquals(self.term_and_condition.users.all().count(),2)
        self.assertQuerysetEqual(self.term_and_condition.users.all(),User.objects.filter(userterms__terms=self.term_and_condition),ordered=False)


    def test_get_term_and_condition_actual(self):
        term_and_condition_2 = TermsAndConditions.objects.create(
            name = "Termo e Condição 2",
            date_active = timezone.now()
        )
        self.assertEqual(term_and_condition_2,TermsAndConditions.get_active())
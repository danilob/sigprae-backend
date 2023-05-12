from django.test import TestCase


from category.models import Category, Subject

class TestUser(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(
            name = "Biologia"
        )
        self.category2 = Category.objects.create(
            name = "Matemática"
        )
        self.category3 = Category.objects.create(
            name = "Ciência da Computação"
        )
        self.category4 = Category.objects.create(
            name = "Psicologia"
        )
        self.subject1 = Subject.objects.create(
            description="Estatística"
        )
        self.subject2 = Subject.objects.create(
            description="Didática"
        )
        self.subject3 = Subject.objects.create(
            description="Programação"
        )
        self.subject1.categories.add(self.category1)
        self.subject1.categories.add(self.category2)
        self.subject1.categories.add(self.category3)

        self.subject2.categories.add(self.category1)
        self.subject2.categories.add(self.category2)

        self.subject3.categories.add(self.category3)

    def test_get_list_subjects(self):
        self.assertCountEqual(self.category1.get_list_subjects(),["Estatística","Didática"])
        self.assertCountEqual(self.category2.get_list_subjects(),["Estatística","Didática"])
        self.assertCountEqual(self.category3.get_list_subjects(),["Estatística","Programação"])
        self.assertCountEqual(self.category4.get_list_subjects(),[])

    def test_get_list_categories(self):
        self.assertCountEqual(self.subject1.get_list_categories(),["Biologia","Matemática", "Ciência da Computação"])
        self.assertCountEqual(self.subject2.get_list_categories(),["Biologia","Matemática"])
        self.assertCountEqual(self.subject3.get_list_categories(),["Ciência da Computação"])
    

    def test_count_subjects(self):
        self.assertEqual(Subject.count_subjects(),3)
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import Choice, Menu, Option, Sizes

class MenuModelTests(TestCase):
    def test_returns_expected_name(self):
        """
        name() returns a string formated like "Today's Menu (Monday 06 August 2018)" with the
        date of the menu.
        """
        date = timezone.now()
        menu = Menu(date=date)

        self.assertEqual('Today\'s Menu (' + date.strftime('%A %d %B %Y') + ')', menu.name())

    def test_str_returns_name(self):
        """
        __str__ returns the string from name() method
        """
        menu = Menu(date=timezone.now())

        self.assertEqual(str(menu), menu.name())


class OptionModelTests(TestCase):
    def test_str_returns_name(self):
        """
        __str__ returns the model's name attribute
        """
        menu = Menu(date=timezone.now())
        option = Option(menu=menu, description="Food description", name="Name")

        self.assertEqual(str(option), option.name)


class  ChoiceModelTests(TestCase):
    def test_sets_default_size(self):
        menu = Menu(date=timezone.now())
        option = Option(menu=menu, description="Food description", name="Name")
        eater = User.objects.create_user(
            username='Username', email='email@example.com', password='password'
        )
        choice = Choice(eater=eater, option=option, preferences="No sugar") 

        self.assertEqual(choice.size.value, 'Normal')

    def test_gets_specified_size(self):
        menu = Menu(date=timezone.now())
        option = Option(menu=menu, description="Food description", name="Name")
        eater = User.objects.create_user(
            username='Username', email='email@example.com', password='password'
        )
        choice = Choice(eater=eater, option=option, preferences="No sugar", size=Sizes.XL) 

        self.assertEqual(choice.size.value, 'Extra Large')

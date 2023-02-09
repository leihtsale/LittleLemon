from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from restaurant import views


MENUITEM_URL = '/restaurant/menu'


def create_menuitem(**kwargs):
    return MenuItem.objects.create(**kwargs)


def create_user(**kwargs):
    return get_user_model().objects.create(**kwargs)


class MenuItemViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.user = create_user(
            username='testuser',
            password='testpass'
        )

        create_menuitem(
            title="Ice Cream",
            price=60,
            inventory=100,
        )
        create_menuitem(
            title="Apple Pie",
            price=10,
            inventory=10,
        )
        create_menuitem(
            title="Almond Malai Kulfi",
            price=40,
            inventory=50,
        )
        create_menuitem(
            title="Lemon Tart",
            price=20.5,
            inventory=5,
        )
        create_menuitem(
            title="Pistachio Phirni",
            price=5.25,
            inventory=150,
        )

    def test_getall(self):
        items = MenuItem.objects.all()
        serialized = MenuItemSerializer(items, many=True)

        request = self.factory.get(MENUITEM_URL)
        request.user = self.user
        response = views.MenuItemView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(serialized.data, response.data)

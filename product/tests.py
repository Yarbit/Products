from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
from product.models import Product, Category


class LastViewTests(TestCase):
    @staticmethod
    def get_logined_user():  # method return logined user
        client = Client()
        user = User.objects.create_user('test_user', password='test_user')
        # self.client.login(username='test_user', password='test_user')
        client.force_login(user)  # simulate login
        return client

    def test_view_last_require_authorization(self):
        # test not authorized user
        response = self.client.get(reverse('last_24_hours'))
        self.assertEqual(response.status_code, 302)

        # test authorized user
        client = self.get_logined_user()
        response = client.get(reverse('last_24_hours'))  # get view that /last/
        self.assertEqual(response.status_code, 200, msg='User not authorized')

    def test_view_last_with_no_products(self):
        """
        If no last products exist, an appropriate message should be displayed.
        """
        client = self.get_logined_user()
        response = client.get('/products/last/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No products.")
        self.assertQuerysetEqual(response.context['products'], [], "Products list must be empty!")

    # test view with one product
    def test_view_last_with_one_product(self):
        datetime_now = timezone.now()
        datetime_after_24_hours = datetime_now + timezone.timedelta(hours=24)  # time after 24 hours

        # create category and product for testing
        category = Category.objects.create(name="test_category", description="")
        Product.objects.create(name="test_product", description="", price=0, category=category)

        client = self.get_logined_user()
        response = client.get(reverse('last_24_hours'))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No products.")  # with one product view musn't contains this message
        self.assertQuerysetEqual(response.context['products'], ['<Product: test_product>'])

        # since querysets are equal, get first product from result set
        result_product = response.context['products'][0]

        # assert that product was created 24 hours ago
        self.assertTrue(datetime_now <= result_product.created_at <= datetime_after_24_hours,
                        "Product 'created_at' out of bounds")

        # assert that product wouldn`t be in queryset after 1 minute
        self.assertFalse(datetime_now + timezone.timedelta(
            minutes=1) <= result_product.created_at <= datetime_after_24_hours + timezone.timedelta(minutes=1))

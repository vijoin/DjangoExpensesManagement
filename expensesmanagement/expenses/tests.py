from django.contrib.auth.models import User
from django.test import TestCase
from .models import Expense
from products.models import Product

class ExpenseTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='unittest')
        product = Product.objects.create(name='Tomato')
        Expense.objects.create(user_id=user, product_id=product, amount=300)
        #expense = Expense.objects.create(user_id=user, amount=300)

    def test_expense_creation(self):
        user = User.objects.get(username='unittest')
        product = Product.objects.get(name='Tomato')
        expense = Expense.objects.get(amount=300, user_id=user, product_id=product)
        #expense = Expense.objects.get(amount=300, user_id=user)
        self.assertEqual(expense.amount, 300)

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_base_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, template_name='base.html')

    def test_monthly_expenses_report(self):
        endpoint = '/expenses/report/2019/12'
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)

    def test_monthly_expenses_report_template(self):
        endpoint = '/expenses/report/2019/12'
        response = self.client.get(endpoint)
        self.assertTemplateUsed(response, template_name='monthly_report.html')

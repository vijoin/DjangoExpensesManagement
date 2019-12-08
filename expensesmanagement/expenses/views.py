from django.shortcuts import render

from expenses.models import Expense


def report_monthly_expenses(request, year, month):
    data = {'year': year, 'month': month}
    expenses = Expense.objects.filter(date__year=year, date__month=month)
    return render(request, 'monthly_report.html', {'expenses': expenses, 'data': data})

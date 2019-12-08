from django.shortcuts import render

def report_monthly_expenses(request, year, month):
    data = {
        'year': year,
        'month': month,
        }
    return render(request, 'monthly_report.html', {'data': data})

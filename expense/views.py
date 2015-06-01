from django.http import HttpResponse
from django.db.models import Sum, Q
from django.utils import simplejson
from django.contrib.auth.models import User
from django.template import Context, loader
from django.conf import settings
import models

def bar_chart_data(request, user_id, type, year, month):
    expense_type =  models.Type.objects.get(id = type)
    data =  _get_bar_chart_data(expense_type, user_id, year, month)
    labels =  []
    index = 0
    for c in expense_type.categories.all().order_by('name'):
        labels.append([index, c.name])
        index = index + 1

    t = loader.get_template('admin/expense/expense/bar_chart.html')
    c = Context({
        'media_dir': settings.MEDIA_URL + "/expense/",
        'type': expense_type.name,
        'year':  year,
        'month': month,
        'chart_data': simplejson.dumps(data),
        'labels': simplejson.dumps(labels),
    })
    return HttpResponse(t.render(c))

def _get_bar_chart_data(type, user_id=None, year = None, month = None):
    results = []
    users = []
    q = Q()
    if year and int(year) > 0:
        q = q & Q(date__year = year)
    if month and int(month) > 0:
        q =  q & Q(date__month = month)

    if user_id and int(user_id) > 0:
        users.append(User.objects.get(id=user_id));
    else:
        users = User.objects.all()

    for u in users:
        user_data = []
        user_filter =  q & Q(user = u)
        index = 0
        for c in type.categories.all().order_by('name'):
            sub_total = c.expenses.filter(user_filter).aggregate(
                total = Sum('amount'))

            if(sub_total["total"]):
                user_data.append([index, sub_total["total"]])
            else:
                user_data.append([index, 0])

            index = index + 1
        results.append({'label': u.username, 'data': user_data})

    return results

def pie_chart_data(request, user_id, type, year, month):
    expense_type =  models.Type.objects.get(id = type)
    data =  _get_pie_chart_data(expense_type, user_id, year, month)
    t = loader.get_template('admin/expense/expense/pie_chart.html')
    c = Context({
        'media_dir': settings.MEDIA_URL + "/expense/",
        'type': expense_type.name,
        'year':  year,
        'month': month,
        'chart_data': simplejson.dumps(data),
    })
    return HttpResponse(t.render(c))

def _get_pie_chart_data(type, user_id=None, year = None, month = None):
    results = []
    q = Q()
    if user_id and int(user_id) > 0:
        q = Q(expenses__user__id = user_id)
    if year and int(year) > 0:
        q = q & Q(expenses__date__year = year)
    if month and int(month) > 0:
        q = q & Q(expenses__date__month = month)

    #calculate values

    type.category_list = type.categories.filter(q).annotate(
        category_total = Sum('expenses__amount'))

    #format the results
    for c in type.category_list:
        results.append({
                'label': c.name,
                'data': c.category_total
                })

    return results




import models as m
from django.db import models
from django.db.models import Sum, Q

class TypeManager(models.Manager):
    """
    Manager class of Type objects.
    """
    def get_statistics(self, user_id, year, month):
        """
        Creates a statistic query by the given parameters.
        """
        types =  m.Type.objects.all()
        cat_filter = Q()
        if user_id:
            cat_filter = Q(expenses__user__id = user_id)
        if year:
            cat_filter = cat_filter & Q(expenses__date__year = year)
        if month:
            cat_filter =  cat_filter & Q(expenses__date__month = month)

        for t in types:
            t.category_list = t.categories.filter(cat_filter).annotate(
                category_total = Sum('expenses__amount'))

            total = t.category_list.aggregate(total = Sum('category_total'))
            t.total =  total['total']
        return types

class ExpenseManager(models.Manager):
    """
    Manager class of Expense objects.
    """
    def get_months(self):
        """
        Return the list of the months where expense objects are
        recorded.
        """
        return m.Expense.objects.dates('date', 'month', order='DESC')

    def get_years(self):
        """
        Returns the list of the where expense objects are
        recorded.
        """
        return m.Expense.objects.dates('date', 'year', order='DESC')


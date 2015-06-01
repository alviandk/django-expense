from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from managers import *
from templatetags import numberformat

class Type(models.Model):
    """
    Expense groups are represented by this model.
    """
    name = models.CharField(_('name'), max_length=50)

    objects = TypeManager()

    class Meta:
        verbose_name_plural = _('types')
        verbose_name = _('type')
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Category(models.Model):
    """
    Expense categories are represented by this model.
    """
    name = models.CharField(_('name'), max_length=50)
    type = models.ForeignKey(Type, related_name='categories',
                             blank = False, null=True)

    class Meta:
        verbose_name_plural = _('categories')
        verbose_name = _('category')
        ordering = ['type__name', 'name']

    def __unicode__(self):
        return ("%s - %s" % (self.type.name,  self.name))

    def type_name(self):
        return self.type.name

class Expense(models.Model):
    """
    Expenses are represented by this model.
    """
    user = models.ForeignKey(User, blank = False, null=True)
    category = models.ForeignKey(Category, related_name='expenses', blank=True, null=True)
    date = models.DateField(_('date'), 'date')
    description = models.CharField(_('description'), max_length = 300)
    amount = models.IntegerField(_('amount'))

    objects = ExpenseManager()

    date.expense_date_filter =  True
    class Meta:
        verbose_name_plural = _('expenses')
        verbose_name = _('expense')
        ordering = ['-date', 'category__type__name', 'category__name']

    def __unicode__(self):
        return self.description

    def formatted_amount(self):
        return ('<div class="number">%s</div>' % (numberformat.numberformat(self.amount), ))

    formatted_amount.short_description = _('amount')
    formatted_amount.allow_tags = True

    def date_str(self):
        """
        Formats the date by "%Y-%m-%d." pattern.
        """
        # How do you internationalize date strings? We'll just use ISO
        # 8601 format.
        return self.date.strftime("%Y-%m-%d")

    date_str.short_description = _("date")

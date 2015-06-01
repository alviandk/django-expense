# -*- coding: utf-8 -*-

from models import Type, Category, Expense
from django.contrib.auth.models import User
from django.test import TestCase
import datetime
import views

class ModelTestCase(TestCase):
    fixtures = ['users.xml', 'initial_data.json']
    def setUp(self):
        self.category = Category.objects.get(id=1)
        self.user = User.objects.get(id = 100)
        self.expense = Expense.objects.create(
            user=self.user,
            category = self.category,
            date = '2011-01-05',
            description = 'expense',
            amount = 100)

    def tearDown(self):
        [obj.delete() for obj in Expense.objects.all()]

    def testType(self):
        type = Type.objects.get(id = 1)
        self.assertEqual(type.id, 1)
        self.assertEqual(type.name, u'Expenses')

    def testCategory(self):
        category = Category.objects.get(id = 1)
        self.assertEqual(category.name, u'Car')

    def testExpense(self):
        expense = Expense.objects.get(id = 1)
        self.assertEqual(expense.id, 1)
        self.assertEqual(expense.user, self.user)
        self.assertEqual(expense.category, self.category)
        self.assertEqual(expense.description, 'expense')
        self.assertEqual(expense.amount, 100)
        self.assertEqual(expense.date, datetime.date(2011, 1, 5))


class ExpenseCalculationTestCase(TestCase):
    fixtures = ['users.xml', 'initial_data.json']
    def setUp(self):
        # clean up the expense database
        [obj.delete() for obj in Expense.objects.all()]
        # create objects

        self.category_1 = Category.objects.get(id=1)
        self.category_2 = Category.objects.get(id=2)
        self.user_1 = User.objects.get(id=100)
        self.user_2 = User.objects.get(id=101)
        Expense.objects.create(user=self.user_1,
                               category = self.category_1,
                               date = '2009-02-05',
                               description = 'expense 1',
                               amount = '100')
        Expense.objects.create(user=self.user_1,
                               category = self.category_1,
                               date = '2009-02-05',
                               description = 'expense 2',
                               amount = '100')
        Expense.objects.create(user=self.user_1,
                               category = self.category_2,
                               date = '2009-02-05',
                               description = 'expense 3',
                               amount = '100')
        Expense.objects.create(user=self.user_2,
                               category = self.category_2,
                               date = '2009-02-05',
                               description = 'expense 4',
                               amount = '100')
    def tearDown(self):
        # remove objects from db
        [obj.delete() for obj in Expense.objects.all()]

    def testStatisticsForUser1(self):
        # check type list
        type_list = Type.objects.get_statistics(100, 2009, 2)
        category_list = type_list[0].category_list
        # check amount calculations
        self.failUnlessEqual(category_list[0].category_total, 200)
        self.failUnlessEqual(category_list[1].category_total, 100)

    def testStatisticsForUser2(self):
        # check type list
        type_list = Type.objects.get_statistics(101, 2009, 2)
        category_list = type_list[0].category_list
        # check amount calculations
        # category 1 is not visible for user 2 so the list will conatin
        # only 'category 2'
        self.failUnlessEqual(len(category_list), 1)
        self.failUnlessEqual(category_list[0].category_total, 100)


    def testYears(self):
        years = Expense.objects.get_years()
        self.failUnlessEqual(len(years), 1)
        self.failUnlessEqual(years[0].year, 2009)

    def testMonths(self):
        months = Expense.objects.get_months()
        self.failUnlessEqual(len(months), 1)
        self.failUnlessEqual(months[0].year, 2009)
        self.failUnlessEqual(months[0].month, 2)

    def testChartAllData(self):
        t = Type.objects.get(id=1)
        data = views._get_chart_data(t, 0, 0, 0)
        self.failUnlessEqual(len(data), 2)
        #user 1
        self.failUnlessEqual(data[0]["data"], [[7, 0], [1, 200], [4, 0], [5, 0], [2, 100], [3, 0], [6, 0]])
        self.failUnlessEqual(data[0]["label"], u"super")
        #user 2
        self.failUnlessEqual(data[1]["data"], [[7, 0], [1, 0], [4, 0], [5, 0], [2, 100], [3, 0], [6, 0]])
        self.failUnlessEqual(data[1]["label"], u"super2")

    def testChartOneUser(self):
        t = Type.objects.get(id=1)
        data = views._get_chart_data(t, 100, 0, 0)
        self.failUnlessEqual(len(data), 1)
        #user 1
        self.failUnlessEqual(data[0]["data"], [[7, 0], [1, 200], [4, 0], [5, 0], [2, 100], [3, 0], [6, 0]])
        self.failUnlessEqual(data[0]["label"], u"super")

    def testChartNoData(self):
        t = Type.objects.get(id=1)
        data = views._get_chart_data(t, 100, 2034, 1)
        self.failUnlessEqual(len(data), 1)
        self.failUnlessEqual(data[0]["data"], [[7, 0], [1, 0], [4, 0], [5, 0], [2, 0], [3, 0], [6, 0]])
        self.failUnlessEqual(data[0]["label"], u"super")


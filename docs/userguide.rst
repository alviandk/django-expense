.. _userguide:

User guide
==========

Introduction
------------

When you finished installation, django-expense will appear on your
Django admin site. From the admin menu you can edit three types of
entities:

* **Type**: These are the Expense basic types such as income, outcome, savings etc... or you can use as bank account as well.

* **Categories**: These are the sub-categories under each type such as outcome/household, etc...

* **Expenses**: These are the expense items. 
   

Main screen, expense list
------------------------

The Expense change_list view is extended by a simple report, this page
by default shows your expenses for the current month and summarizes
your items by categories. Using the filters of the right hand side you
can change the default filter expressions. You can filter the list by:

* Users: Individual user or all.
* Date: Month, year, all time.
* Category

The following figure shows the main screen of the application:

.. figure:: images/main.*
   :width: 730px
   :alt: Main screen
   :align: center

Add expense screen
-------------------

Expenses can be added on this screen. The user field is defaulted with
the currently logged on one, otherwise it is a default django admin
screen.

.. figure:: images/add.*
   :alt: Add expense screen
   :align: center


Reports
-------

On the report screen, expenses are displayed with a pie or a stacked bar
chart. The filter conditions of the reports are inherited from the
expense list screen, so if you change the filters on the list screen
the chart will be display data to that filter conditions.

Charts are using `flot <http://code.google.com/p/flot/>`_ `jQuery <http://jquery.com/>`_ plugin.

The following figure shows a sample pie chart from the application:

.. figure:: images/pie_chart.*
   :alt: Report screen
   :align: center


And a sample stacked bar chart:

.. figure:: images/bar_chart.*
   :alt: Report screen
   :align: center



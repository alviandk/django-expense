.. _installation:

Installation
============

Before installing django-expense, you'll need to have a copy of
`Django <http://www.djangoproject.com>`_ already installed. Django
version 1.4 is required. 

.. note:: If you need Django 1.3 support, use version 0.2.2.

For further information, consult the `Django download page
<http://www.djangoproject.com/download/>`_, which offers convenient
packaged downloads and installation instructions.

Installation from source code and using development server
----------------------------------------------------------

Getting the code
~~~~~~~~~~~~~~~~

If you would like to try out the latest in-development code, you can
obtain it from the django-expense repository, which is hosted at
`Bitbucket <http://bitbucket.org/>`_ and uses `Mercurial
<http://www.selenic.com/mercurial/wiki/>`_ for version control. To
get the latest code and documentation type the following commands::

    hg clone http://bitbucket.org/szunyog/django-expense/

This will create a copy of the django-expense Mercurial
repository on your computer.

Or you can download the source code from the `downloads
<https://bitbucket.org/szunyog/django-expense/downloads>`_ page. Use
the **tip** tag for the latest release.

Starting the development server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A sample test project is included into the source tree, so if you want
to try you can simple start this test project, to do this you need to
enter the following commands::

  cd testapp
  python manage.py syncdb
  python manage.py runserver

.. note:: The development server is configured to use `sqlite <http://www.sqlite.org/>`_ database, so required packages should be installed.


Installation from package
-------------------------

Download the package
~~~~~~~~~~~~~~~~~~~~

You can download the source code from the `downloads
<https://bitbucket.org/szunyog/django-expense/downloads>`_ page. Use
the **tip** tag for the latest release.

Install
~~~~~~~

Once you've downloaded the package, from a command line in that
directory, type::

    python setup.py install

.. note:: On some systems you may need to execute this with administrative privileges (e.g., ``sudo python setup.py install``).

Required settings
~~~~~~~~~~~~~~~~~

Begin by adding ``'django.contrib.admin`` and ``expense`` to the
``INSTALLED_APPS`` setting of your project:

For example, you might have something like the following in your
Django settings file::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.sites',
	'django.contrib.admin',
        'expense',
        # ...other installed applications...
    )

Once you've done this, run ``manage.py syncdb`` to install the model
used by the default setup.


Setting up URLs
~~~~~~~~~~~~~~~

Expense application working on Django admin interface, so you have to
enable it in your ``urls.py``::

   from django.contrib import admin
   admin.autodiscover()
   urlpatterns = patterns('',
      # Set up static files, you can do it with you web server configuration.
      # Dont forget to check if your envrioment installed it to the same
      # location as the example shows.
      (r'^static/media/expense(?P<path>.*)$',
         'django.views.static.serve',{
      	     'document_root': '/usr/local/lib/python2.6/dist-packages/expense/static/expense/',
          'show_indexes': True }),
       # set up expense's urls
       (r'^expense/', include('expense.urls')),
       (r'^', include(admin.site.urls)),
   )

.. note:: Using this URL configuration your django admin site will be in the root.


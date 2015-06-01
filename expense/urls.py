from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns(
    'expense.views',
    url(r'^bar_chart_data/(?P<user_id>\d+)/(?P<type>\d+)/(?P<year>\d+)/(?P<month>\d+)',
        views.bar_chart_data),
    url(r'^pie_chart_data/(?P<user_id>\d+)/(?P<type>\d+)/(?P<year>\d+)/(?P<month>\d+)',
        views.pie_chart_data),
)


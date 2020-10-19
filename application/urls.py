from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='home'),
    path('vote/', views.vote, name='vote'),
    path('check-vote-registration/', views.check_vote, name='check-vote'),
    path('request-absentee-ballot/', views.absentee_ballot, name='absentee-ballot'),
    path('election-reminder/', views.election_reminder, name='election-reminder'),
    path('pledge-to-register/', views.pledge_register, name='pledge-register'),

]
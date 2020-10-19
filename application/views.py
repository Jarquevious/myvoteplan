from django.shortcuts import render
from django.http import HttpResponse
from .form import QuestionForm
from django.http import HttpResponse
from .models import Question
import requests, json



def index(request):
    # representative()
    electioninfo = get_electionInfo()
    locations = electioninfo["pollingLocations"]

    print(json.dumps(locations, indent=4))
    
    context = {"locations": locations,
                "electionInfo": electioninfo    
            }
    # get_elections()
    # find_election()
    return render(request, 'application/index.html', context)

def vote(request):
    return render(request, 'application/vote-register.html')

def check_vote(request):
    return render(request, 'application/vote-check.html')

def absentee_ballot(request):
    return render(request, 'application/absentee-ballot.html')

def election_reminder(request):
    return render(request, 'application/election-reminder.html')

def pledge_register(request):
    return render(request, 'application/pledge-register.html')


def find_election(query="president"):
    url = "https://www.googleapis.com/civicinfo/v2/divisions"

    querystring = {
                    "key":"AIzaSyDID0q9BHOlG-8m_xgMd3-1tcqZiHXwZWs",
                    "query": query,
                }

    headers = {
        "key":"AIzaSyDID0q9BHOlG-8m_xgMd3-1tcqZiHXwZWs",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return response.json

def get_representatives_by_address():
    url = "https://www.googleapis.com/civicinfo/v2/representatives"

    querystring = {
                    "key":"AIzaSyDID0q9BHOlG-8m_xgMd3-1tcqZiHXwZWs",
                    "address": "94108",
                    "levels": "country",
                    "roles": "legislatorUpperBody",
                    "roles": "legislatorLowerBody",
                }

    headers = {
        "key":"AIzaSyDID0q9BHOlG-8m_xgMd3-1tcqZiHXwZWs",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return response.json

def get_elections():
    url = "https://www.googleapis.com/civicinfo/v2/elections"

    querystring = {
                    "key":"AIzaSyDID0q9BHOlG-8m_xgMd3-1tcqZiHXwZWs",
                }

    headers = {
        "key":"AIzaSyDID0q9BHOlG-8m_xgMd3-1tcqZiHXwZWs",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return response.json

def get_electionInfo():
    url = "https://www.googleapis.com/civicinfo/v2/voterinfo"

    querystring = {
                    "key":"AIzaSyDID0q9BHOlG-8m_xgMd3-1tcqZiHXwZWs",
                    "address": "851 california st. san francisco, ca 94108",

                }

    headers = {
        "key":"AIzaSyDID0q9BHOlG-8m_xgMd3-1tcqZiHXwZWs",
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    return response.json()




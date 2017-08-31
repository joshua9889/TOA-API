# -*- coding: UTF-8 -*-
__author__ = 'joshua9889' 
 
import json 
import urllib 
import socket
import webbrowser
import logging
from urllib import request as REQUEST

Application_Origin = 'stop'
TOA_Key = 'go get your own'

Dev_URL = 'https://dev.theyellowalliance.com/api'
Beta_URL = 'https://beta.theorangealliance.org/api'
use_dev = False

try: 
    socket.setdefaulttimeout(3) 
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
    connected_to_internet = True
except Exception as ex:
    print('Cannot connect to internet. Please try again later.') 
    connected_to_internet = False

def setApplicationOrigin_TOAKey(AppOrigin, TOA_Key_):
    Application_Origin = str(AppOrigin)
    TOA_Key = TOA_Key_

#opens API doc
def help_me(): 
    if connected_to_internet: 
        webbrowser.open_new('https://docs.google.com/document/d/1vtoNmTh7mlc-HTa4irrHNa6pthhvNScMoLFVrzPXEmw/edit') 
 
#Returns full json 
def pull_request(request_code): 
    if connected_to_internet:
        request = REQUEST.Request(Beta_URL + str(request_code))
        if use_dev:
            request = REQUEST.Request(Dev_URL + str(request_code))
        else:
            reqest = REQUEST.Request(Beta_URL + str(request_code))
        request.add_header('X-Application-Origin', Application_Origin) 
        request.add_header('X-TOA-Key', TOA_Key) 
        
        reponse = REQUEST.urlopen(request)
        return json.dumps(json.loads(reponse.read())) 

class Team():
    #Returns specific json value given a team number
    def get_json(team_number, json_value): 
        if connected_to_internet: 
            json_ = json.loads(pull_request('/team/' + str(team_number))) 
            return json_[0][str(json_value)]

    #Return Team Key
    def key(team_number):
        return Team.get_json(team_number, 'team_key')
    
    #Return Team name given a team number
    def name(team_number):
        team_name = Team.get_json(team_number, 'team_name_short')
        if str(team_name) == 'None':
            team_name = Team.get_json(team_number, 'team_name_long')
        return team_name

    #Return Region Key given a team number
    def regionKey(team_number):
        return Team.get_json(team_number, 'region_key')

    #Return League Key given a team number
    def leagueKey(team_number):
        return Team.get_json(team_number, 'league_key')

    #Return Robot Name given a team number
    def robotName(team_number):
        return Team.get_json(team_number, 'robot_name')

    #Return City given a team number
    def city(team_number):
        return Team.get_json(team_number, 'city')

    #Return State given a team number
    def state(team_number):
        return Team.get_json(team_number, 'state_prov')

    #Guess what this does
    def country(team_number):
        return Team.get_json(team_number, 'country')

    #I'm sorry, but if you can't figure out what this does you may need to see a doctor
    def rookieYear(team_number):
        return Team.get_json(team_number, 'rookie_year')

    #Return website
    def website(team_number):
        return Team.get_json(team_number, 'website')

    def eventsAttended(team_number,year=2017):
        return pull_request('/team/'+str(team_number)+'/'+str(year)+'/events/')

    def results(team_number,year=2017):
        return pull_request('/team/'+str(team_number)+'/'+str(year)+'/results/')

    #Returns all awards won by the tean in the year specified
    def awards(team_number,year=2017):
        return pull_request('/team/'+str(team_number)+'/'+str(year)+'/awards/')

    #Returns amount of teams
    def count():
        json_ = json.loads(pull_request('/teams/count/'))
        return json_[0]["TeamsCount"]

#All methods for any event is here
class Event():
    #get full json from an event
    def get_json(event_key, json_value):
        if connected_to_internet:
            json_ = json.loads(pull_request('/event/'+str(event_key))) 
            return json_[0][str(json_value)]

    def seasonKey(event_key):
        return Event.get_json(event_key, 'season_key')
    
    def regionKey(event_key):
        return Event.get_json(event_key, 'region_key')

    def leagueKey(event_key):
        return Event.get_json(event_key, 'league_key')

    def code(event_key):
        return Event.get_json(event_key, 'event_code')

    def regionNumber(event_key):
        return Event.get_json(event_key, 'event_region_number')

    def divisionId(event_key):
        return Event.get_json(event_key, 'division_id')

    def divisionName(event_key):
        return Event.get_json(event_key, 'division_name')

    def type(event_key):
        return Event.get_json(event_key, 'event_type')

    def name(event_key):
        return Event.get_json(event_key, 'event_name')

    def startDate(event_key):
        return Event.get_json(event_key, 'start_date')

    def endData(event_key):
        return Event.get_json(event_key, 'end_data')

    def weekKey(event_key):
        return Event.get_json(event_key, 'week_key')

    def city(event_key):
        return Event.get_json(event_key, 'city')

    def stateProv(event_key):
        return Event.get_json(event_key, 'state_prov')

    def country(event_key):
        return Event.get_json(event_key, 'country')

    def venue(event_key):
        return Event.get_json(event_key, 'venue')

    def website(event_key):
        return Event.get_json(event_key, 'event_website')

    def timeZone(event_key):
        return Event.get_json(event_key, 'time_zone')

    def tournmentLevel(event_key):
        return Event.get_json(event_key, 'tournment_level')

    def allianceCount(event_key):
        return Event.get_json(event_key, 'alliance_count')

    def fields(event_key):
        return Event.get_json(event_key, 'fields')

    def advancementSpots(event_key):
        return Event.get_json(event_key, 'advancement_spots')

    def advancementEvent(event_key):
        return str(Event.get_json(event_key, 'advancement_event')) != None

    def TeamsAttending(event_key):
        year = event_key[:4]
        return pull_request('/event/'+str(year)+'/' + str(event_key) + '/teams')

    def allEvents():
        return pull_request('/events/')

    def regionEvents(region_id):
        return pull_request('/events/region/'+str(region_id))

    def typeEvents(event_type):
        return pull_request('/events/type/'+str(event_type))

    def leagueEvents(league_id):
        return pull_request('/events/league/' + str(league_id))

    def rankings(event_key):
        year = '20' + str(event_key[2:4])
        return pull_request('/event/'+ str(year)+'/'+str(event_key)+'/rankings')

    def allMatchData(event_key):
        year = '20' + str(event_key[2:4])
        return pull_request('/event/'+ str(year)+'/'+str(event_key)+'/matches')

    def awards(event_key):
        year = '20' + str(event_key[2:4])
        return pull_request('/event/'+str(year)+'/'+str(event_key)+'/awards')
    
#Get Match data
class Match():
    def details(year, match_key):
        return pull_request('/' +str(year)+ '/'+str(match_key)+ '/details')
    
    def numOfMatches(year=2017):
        if connected_to_internet: 
            try:
                json_ = json.loads(pull_request('/matches/'+str(year)+ '/count/')) 
                return json_[0][str('MatchCount')]
            except:
                print("Try a different year. Maybe that will fix it.")

    #TOA API currently does not work with this request           
    def highScoreNoPenalties(year = 2017):
        if connected_to_internet:
            try:
                return str(pull_request('/matches/'+ str(year)+'/high-scores/no-penalty'))
            except:
                return False

    def highScoreWithPenalties(year = 2017):
        if connected_to_internet:
            try:
                return str(pull_request('/matches/'+ str(year) + '/high-scores/with-penalty'))
            except:
                print('sry bout dat')
                print("TOA isn't workin'")


if Match.highScoreNoPenalties() == False:
    logging.warning('TOA is still broken')

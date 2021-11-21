import requests
from infoAccess import *
import factory

class siteService():

    def __init__(self):
        host = "127.0.0.1"
        port = 3306
        user = "root"
        password = "qz987270"
        database = "KeepFeel"
        self.siteAccess = infoAccess(host, port, user, password, database)
    
    def siteSearch(self, msg):
        location_lat, location_lng, query = msg["user_latitude"], msg["user_longitude"], msg["keyword"]
        results = self.baidu_search(location_lng, location_lat, query)
        site_info = []
        for res in results:
            # todo: check personNum
            res["personNum"] = 0 #self.checkNum(res["name"])
            site_info.append(res.copy())

        return site_info

    def baidu_search(self, location_lng, location_lat, query):
        url = 'http://api.map.baidu.com/place/v2/search?'
        radius = '5000'         #搜索半径，单位为m
        output = 'json'
        ak = 'CEBjSg6aSNzGGe0tEfcA83MNRh1r02wY'         #密钥
        uri = url + 'query=' + query + '&location='+location_lat+','+location_lng+'&radius='+radius+'&output=' + output + '&ak=' + ak
        print(uri)
        r = requests.get(uri)
        response_dict = r.json()
        print(response_dict)
        results = response_dict["results"]
        result = []
        adr = {}
        for adrs in results:
            adr['name'] = adrs['name']
            adr['location'] = adrs['address']
            result.append(adr.copy())

        return result
    
    def checkNum(self, siteName):
        query = {}
        query["sportsLocations"] = siteName
        query["sportsType"] = None
        sites = self.siteAccess.query_match(query)

        return len(sites)

    def querySite(self, site):
        result = self.siteAccess.query_site(site)
        if len(result) == 0:
            return False

        return True
    
    def addNewSite(self, site):
        self.siteAccess.insert_site(site)
    
    def updateSiteInfo(self, site):
        self.siteAccess.update_site(site)


class personService():

    def __init__(self):
        host = "127.0.0.1"
        port = 3306
        user = "root"
        password = "qz987270"
        database = "KeepFeel"
        self.personAccess = infoAccess(host, port, user, password, database)
    
    def matchPersonList(self, msg):
        query_info = {}
        sportsLocation, sportsType, startTime, endTime = msg["sportsLocation"], msg["sportsType"], msg["startTime"], msg["endTime"]
        query_info["sportsLocation"] = sportsLocation
        query_info["sportsType"] = sportsType
        userIds = self.personAccess.query_match(query_info)

        person_list = []
        for userId, start, end in userIds:
            if not self.judge(startTime, endTime, start, end): continue
            userId, nickname, gender, _, _ = self.personAccess.query_person(userId)
            person_list.append([userId, nickname, gender])

        return person_list
    
    def viewPersonInfo(self, user):
        person_info  = self.personAccess.query_person(user["userId"])

        return person_info
    
    def updatePersonInfo(self, person):
        self.personAccess.update_person(person)
        return True

    def addNewPerson(self, person):
        self.personAccess.insert_person(person)
        return True
    
    def judge(self, startTime, endTime, start, end):
        # todo: convert string time into int
        def convert(time):
            time = time.split(":")
            return int(time[0]) + int(time[1])/60

        startTime, endTime, start, end = convert(startTime), convert(endTime), convert(start), convert(end)
        if (endTime <= start) or (end <= startTime):
            return False
        
        return True

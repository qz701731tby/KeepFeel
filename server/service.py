import requests
from infoAccess import *
from factory import factory
import base64
import time
import os

class timeSerivce:
    def convert2timestamp(msg):
        '''
            convert the msg time format into timestamp
        '''
        date_str, startTime, endTime = msg["date"], msg["startTime"], msg["endTime"]
        startTime_str = date_str + " " + startTime + ":00"
        endTime_str = date_str + " " + endTime + ":00"
        print("startTime_str:", startTime_str)
        print("endTime_str:", endTime_str)
        startTime = time.mktime(time.strptime(startTime_str,'%Y-%m-%d %H:%M:%S'))
        endTime = time.mktime(time.strptime(endTime_str,'%Y-%m-%d %H:%M:%S'))
        print("startTime:", startTime)
        print("endTime:", endTime)

        return int(startTime), int(endTime)
    
    def compare(startTime, endTime, start, end):
        '''
            judge two periods of time overlap
        '''
        if (endTime <= start) or (end <= startTime):
            return False
        
        return True


class siteService:

    def __init__(self):
        host = "127.0.0.1"
        port = 3306
        user = "root"
        password = "qz987270"
        database = "KeepFeel"
        self.siteAccess = infoAccess(host, port, user, password, database)
    
    def siteSearch(self, msg):
        '''
            return the site info according to msg
        '''
        location_lat, location_lng, query = msg["user_latitude"], msg["user_longitude"], msg["keyword"]
        results = self.baidu_search(location_lng, location_lat, query)
        site_info = []
        for res in results:
            # todo: check personNum
            res["personNum"] = self.checkNum(res["name"], msg["openId"])
            site_info.append(res.copy())

        return site_info

    def baidu_search(self, location_lng, location_lat, query):
        '''
            call the baidu map API, 
        '''
        url = 'http://api.map.baidu.com/place/v2/search?'
        radius = '5000'         #搜索半径，单位为m
        output = 'json'
        ak = 'CEBjSg6aSNzGGe0tEfcA83MNRh1r02wY'         #密钥
        uri = url+'query='+query+'&location='+location_lat+','+location_lng+'&radius='+radius+'&output='+output+'&ak='+ak
        print(uri)
        r = requests.get(uri)
        response_dict = r.json()
        # print(response_dict)
        results = response_dict["results"]
        result = []
        adr = {}
        for adrs in results:
            adr['name'] = adrs['name']
            adr['location'] = adrs['address']
            result.append(adr.copy())

        return result
    
    def checkNum(self, siteName, openId):
        '''
            count the number of person in this site
        '''
        query = {}
        query["SportsLocation"] = siteName
        query["SportsType"] = None
        matches = self.siteAccess.query_match(query)
        visited_ids = []
        person_cnt = 0
        for match in matches:
            if match[0] == openId or match[0] in visited_ids:
                continue
            visited_ids.append(match[0])
            person_cnt += 1

        return person_cnt

    def querySite(self, site):
        result = self.siteAccess.query_site(site)
        if len(result) == 0:
            return False

        return True
    
    def addNewSite(self, site):
        self.siteAccess.insert_site(site)
    
    def updateSiteInfo(self, site):
        self.siteAccess.update_site(site)


class personService:

    def __init__(self):
        host = "127.0.0.1"
        port = 3306
        user = "root"
        password = "qz987270"
        database = "KeepFeel"
        self.appId = "************"
        self.secret = "*********************"
        self.personAccess = infoAccess(host, port, user, password, database)
        self.factory = factory()
        self.image_folder_path = "./user_image"
    
    def queryOpenId(self, msg):
        '''
            query openid from wechat server
        '''
        # print(type(msg["code"]))
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' + self.appId + '&secret=' + self.secret + '&js_code=' + msg["code"] + '&grant_type=authorization_code'
        r = requests.get(url)
        response_dict = r.json()

        return response_dict["openid"]
    
    def storeImage(self, bstr, file_path):
        '''
            write base64 data into server path 
        '''
        if(len(bstr)%3 == 1): 
            bstr += "=="
        elif(len(bstr)%3 == 2): 
            bstr += "=" 

        imgdata = base64.b64decode(bstr)
        file = open(file_path, 'wb')
        file.write(imgdata)
        file.close()
    
    def storePersonImage(self, person):
        '''
            use cur timestamp to generate the image store path and call storeImage()
        '''
        OpenId, avatar, photo = person.getOpenId(), person.getAvatar(), person.getPhoto()
        person_folder = os.path.join(self.image_folder_path, OpenId)
        if not os.path.exists(person_folder):
            os.mkdir(person_folder)
        
        cur_time = int(time.time())

        if avatar != "":
            avatar_path = os.path.join(person_folder, "avatar_%d.jpg" % cur_time)
            self.storeImage(avatar, avatar_path)
            person.setAvatar(avatar_path)
        if photo != "":
            photo_path = os.path.join(person_folder, "photo_%d.jpg" % cur_time)
            self.storeImage(photo, photo_path)
            person.setPhoto(photo_path)

        return person
    
    def matchPersonList(self, msg):
        '''
            select person matched with type, site and time
        '''
        query_type = True
        if "SportsType" not in msg.keys():
            query_type = False

        query_info = {}
        startTime, endTime = "", ""
        if not query_type:
            query_info["SportsType"] = None
        else:
            startTime, endTime = timeSerivce.convert2timestamp(msg)
            query_info["SportsType"] = msg["SportsType"]
        query_info["SportsLocation"] = msg["SportsLocation"]
        openIds = self.personAccess.query_match(query_info)
        
        visited_ids = []
        person_list = []
        for openId, start, end in openIds:
            if openId in visited_ids or openId == msg["openId"]:
                continue
            if (not query_type) or timeSerivce.compare(startTime, endTime, start, end): 
                user = self.personAccess.query_person(openId)
                # print(user, type(user))
                openId, _, nickname, gender, _, avatar, _ = user[0]
                person_list.append({"openId": openId, "nickname": nickname, "gender": gender, "avatar": avatar})
                visited_ids.append(openId)

        return person_list
    
    # def matchPersonList(self, msg):
    #     query_info = {}
    #     if "SportsType" not in msg.keys():
    #         query_info["SportsLocation"] = msg["SportsLocation"]
    #         query_info["SportsType"] = None
    #         query_info["startTime"] = int(time.time())
    #         query_info["endTime"] = time.mktime(time.strptime("2038-12-31 12:00:00",'%Y-%m-%d %H:%M:%S'))
    #     else:
    #         query_info["SportsLocation"] = msg["SportsLocation"]
    #         query_info["SportsType"] = msg["SportsType"]
    #         query_info["startTime"] = timeSerivce.convert2timestamp(msg)
    #         query_info["endTime"] = timeSerivce.convert2timestamp(msg)

    #     openIds = self.personAccess.query_match(query_info)
    #     person_list = []
    #     for openId in openIds:
    #         user = self.personAccess.query_person(openId)
    #         print(user, type(user))
    #         openId, _, nickname, gender, _, avatar, _ = user[0]
    #         person_list.append({"openId": openId, "nickname": nickname, "gender": gender, "avatar": avatar})

    #     return person_list
    
    def insertMatchInfo(self, msg):
        '''
            insert a match record into match_info table
        '''
        match_info = {}
        match_info["startTime"], match_info["endTime"] = timeSerivce.convert2timestamp(msg)
        match_info["openId"], match_info["SportsType"], match_info["SportsLocation"] = msg["openId"], msg["SportsType"], msg["SportsLocation"]
        # match_info = self.factory.generateMatchInfo(msg)
        result = self.personAccess.insert_match(match_info)
        
        return result
    
    def viewPersonInfo(self, openId):
        '''
            get a person's information with his openId
        '''
        person_info  = self.personAccess.query_person(openId)
        if len(person_info) == 0:
            return []
        user = self.factory.generatePerson(person_info[0])
        msg = self.factory.generateMsg(user)

        return msg
    
    def updatePersonInfo(self, person):
        person = self.storePersonImage(person)
        self.personAccess.update_person(person)
        
        return True

    def addNewPerson(self, person):
        # person = self.storePersonImage(person)
        self.personAccess.insert_person(person)

        return self.factory.generateMsg(person)


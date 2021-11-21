from instance import *

class factory:

    def generatePerson(msg):
        userId, nickname, gender, intro, photo = msg["userId"], msg["nickname"], msg["gender"], msg["intro"], msg["photo"]
        user = person(userId, nickname, gender, intro, photo)
        
        return user
    
    def generateSite(msg):
        siteId, siteName, address, sportsType = msg["siteId"], msg["siteName"], msg["address"], msg["sportsType"]
        s = site(siteId, siteName, address, sportsType)

        return s
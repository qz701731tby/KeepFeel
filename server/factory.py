from instance import *
import base64

class factory:
    def __init__(self) -> None:
        pass

    def generatePerson(self, msg):
        if isinstance(msg, str):
            openId, wechatId, nickname, gender, intro, avatar, photo = msg, None, None, 0, None, None, None
        elif isinstance(msg, tuple):
            openId, wechatId, nickname, gender, intro, avatar, photo = msg
        else:
            openId, wechatId, nickname, gender, intro, avatar, photo = msg["openId"], msg["wechatId"], msg["nickname"], msg["gender"], msg["intro"],  msg["avatar"], msg["photo"]
        user = person(openId, wechatId, nickname, gender, intro, avatar, photo)
        
        return user
    
    def generateSite(self, msg):
        siteId, siteName, address, sportsType = msg["siteId"], msg["siteName"], msg["address"], msg["sportsType"]
        s = site(siteId, siteName, address, sportsType)

        return s
    
    def generateMsg(self, person):
        return {"openId": person.getOpenId(), "wechatId": person.getWechatId(), "nickname": person.getNickname(), "gender": person.getGender(), "intro": person.getIntro(), "avatar":person.getAvatar(), "photo":person.getPhoto()}
    
    def generateMatchInfo(self, msg):
        return {"openId": msg["openId"], "SportsType": msg["SportsType"], "SportsLocation": msg["SportsLocation"], "startTime": msg["startTime"], "endTime": msg["endTime"]} 
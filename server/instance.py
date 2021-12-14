from enum import Enum

class person:

    def __init__(self, openId, wechatId=None, nickname=None, gender=None, intro=None, avatar=None, photo=None):
        self.openId = openId
        self.wechatId = wechatId
        self.nickname = nickname
        self.gender = gender
        self.intro = intro
        self.avatar = avatar
        self.photo = photo
    
    def getOpenId(self):
        return self.openId

    def getWechatId(self):
        return self.wechatId
    
    def setWechatId(self, wechatId):
        self.wechatId = wechatId

    def getNickname(self):
        return self.nickname
    
    def setNickname(self, nickname):
        self.nickname = nickname
    
    def getGender(self):
        return self.gender
    
    def setGender(self, gender):
        self.gender = gender
    
    def getIntro(self):
        return self.intro
    
    def setIntro(self, intro):
        self.intro = intro
    
    def getPhoto(self):
        return self.photo
    
    def setPhoto(self, photo):
        self.photo = photo
    
    def getAvatar(self):
        return self.avatar
    
    def setAvatar(self, avatar):
        self.avatar = avatar


class site:

    def __init__(self, siteId, name, address, sportsType):
        self.siteId = siteId
        self.name = name
        self.address = address
        self.sportsType = sportsType
    
    def getSiteId(self):
        return self.siteId
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

    def getSportType(self):
        return self.sportsType


class Message:
    login = '0'
    updatePersonInfo = '1'
    siteSearch = '2'
    viewSitePersonList = '3'
    viewPersonInfo = '4'
    viewMatchPersonList = '5'
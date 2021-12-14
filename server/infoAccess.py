# coding: utf-8
import pymysql
from instance import *

class infoAccess:
    
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    
    def connect_db(self):

        return pymysql.connect(host=self.host,
                            port=self.port,
                            user=self.user,
                            password=self.password,
                            database=self.database)
    
    def insert_person(self, person):
        openId, wechatId, nickname, gender, intro, avatar, photo = person.getOpenId(), person.getWechatId(), person.getNickname(), person.getGender(), person.getIntro(), person.getAvatar(), person.getPhoto()
        con = self.connect_db()
        cur = con.cursor()
        try:
            sql_str = ("INSERT INTO user_info (openId, wechatId, nickname, gender, intro, avatar, photo)" 
                        + " VALUES ('%s', '%s','%s', '%s', '%s', '%s', '%s')" % (openId, wechatId, nickname, gender, intro, avatar, photo))
            print(sql_str)
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            print('Insert USER operation error')
            raise
        finally:
            cur.close()
            con.close()
    
    def update_person(self, person):
        openId, wechatId, nickname, gender, intro, avatar, photo = person.getOpenId(), person.getWechatId(), person.getNickname(), person.getGender(), person.getIntro(), person.getAvatar(), person.getPhoto()
        # print("avatar:", avatar)
        con = self.connect_db()
        cur = con.cursor()
        try:
            prefix = "UPDATE user_info SET "
            mid = []
            if wechatId:
                mid.append("wechatId='%s'"%wechatId)
            if nickname:
                mid.append("nickname='%s'"%nickname)
            if gender:
                mid.append("gender='%s'"%gender)
            if intro:
                mid.append("intro='%s'"%intro)
            if avatar:
                mid.append("avatar='%s'"%avatar)
            if photo:
                mid.append("photo='%s'"%photo)
            mids = ",".join(mid)
            suffix = (" WHERE openId = '%s'" % openId)
            sql_str = prefix + mids + suffix
            print(sql_str)
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            print('Insert USER operation error')
            raise
        finally:
            cur.close()
            con.close()

    def query_person(self, openId):
        sql_str = ("SELECT *" + " FROM user_info WHERE openId = '%s'" % openId)
        print(sql_str)
        con = self.connect_db()
        cur = con.cursor()
        cur.execute(sql_str)
        rows = cur.fetchall()
        cur.close()
        con.close()

        return rows
    
    def insert_site(self, site):
        siteId, name, address, sportsType = site.getSiteId(), site.getName(), site.getAddress(), site.getSportsType()
        con = self.connect_db()
        cur = con.cursor()
        try:
            sql_str = ("INSERT INTO site_info (siteId, name, address, sportsType)" 
                        + " VALUES ('%s', '%s','%s', '%s')" % (siteId, name, address, sportsType))
            print(sql_str)
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            print('Insert USER operation error')
            raise
        finally:
            cur.close()
            con.close()

    # def update_site(self, ):
    
    def query_site(self, site):
        siteId = site.getSiteId()
        sql_str = ("SELECT siteId, name, address, sportsType"
                + " FROM site_info WHERE siteId = '%s'" % siteId)

        print(sql_str)
        con = self.connect_db()
        cur = con.cursor()
        cur.execute(sql_str)
        rows = cur.fetchall()
        cur.close()
        con.close()

        return rows
    
    def insert_match(self, match_info):
        openId, SportsType, SportsLocation, startTime, endTime = match_info["openId"], match_info["SportsType"], match_info["SportsLocation"], match_info["startTime"], match_info["endTime"]
        con = self.connect_db()
        cur = con.cursor()
        try:
            sql_str = ("INSERT INTO match_info (openId,SportsType,SportsLocation,startTime,endTime)" 
                        + " VALUES ('%s', '%s','%s','%s', '%s')" % (openId,SportsType,SportsLocation,startTime,endTime))
            print(sql_str)
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            print('Insert match_info operation error')
            raise
        finally:
            cur.close()
            con.close()
    
    def query_match(self, query):
        SportsType, SportsLocation = query["SportsType"], query["SportsLocation"]
        # print(SportsLocation)
        if SportsType == None:
            condition = ("SportsLocation = '%s'" % SportsLocation)
            # sql_str = "SELECT DISTINCT openId FROM match_info WHERE " + condition
        else:
            condition = ("SportsType = '%s' AND SportsLocation = '%s'" % (SportsType, SportsLocation))
            # sql_str = "SELECT DISTINCT openId, startTime, endTime FROM match_info WHERE " + condition

        sql_str = "SELECT DISTINCT openId, startTime, endTime FROM match_info WHERE " + condition
        # "(StartTime = '%s' OR EndTime = '%s')
        print(sql_str)
        con = self.connect_db()
        cur = con.cursor()
        cur.execute(sql_str)
        rows = cur.fetchall()
        cur.close()
        con.close()

        return rows
    
    # def query_match(self, query):
    #     SportsType, SportsLocation, startTime, endTime = query["SportsType"], query["SportsLocation"], query["startTime"], query["endTime"]


    #     if SportsType == None:
    #         condition = ("SportsLocation = '%s' AND ((endTime <= %d) or (%d <= startTime))" % (SportsLocation, startTime, endTime))
    #     else:
    #         condition = ("SportsType = '%s' AND SportsLocation = '%s' AND NOT ((endTime <= %d) or (end <= %d))" % (SportsType, SportsLocation, startTime, endTime))

    #     sql_str = "SELECT DISTINCT openId FROM match_info WHERE " + condition
    #     # "(StartTime = '%s' OR EndTime = '%s')
    #     print(sql_str)
    #     con = self.connect_db()
    #     cur = con.cursor()
    #     cur.execute(sql_str)
    #     rows = cur.fetchall()
    #     cur.close()
    #     con.close()

    #     return rows

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 3306
    user = "root"
    password = "qz987270"
    database = "KeepFeel"
    db = infoAccess(host, port, user, password, database)
    TBY = person("tby980731",nickname="哈利波童", intro="我是一个热爱有氧运动的法硕小仙女")
    userId = "tby980731"
    db.update_person(TBY)
    print(db.query_person(userId))

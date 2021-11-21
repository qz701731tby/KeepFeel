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
        userId, nickname, gender, intro = person.getUserId(), person.getNickname(), person.getGender(), person.getIntro()
        con = self.connect_db()
        cur = con.cursor()
        try:
            sql_str = ("INSERT INTO usr_info (userId,nickname,gender,intro)" 
                        + " VALUES ('%s', '%s','%s', '%s')" % (userId, nickname, gender, intro))
            print(sql_str)
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            print('Insert USR operation error')
            raise
        finally:
            cur.close()
            con.close()
    
    def update_person(self, person):
        userId, nickname, gender, intro = person.getUserId(), person.getNickname(), person.getGender(), person.getIntro()
        con = self.connect_db()
        cur = con.cursor()
        try:
            prefix = "UPDATE usr_info SET "
            mid = []
            if nickname:
                mid.append("nickname='%s'"%nickname)
            if gender:
                mid.append("gender='%s'"%gender)
            if intro:
                mid.append("intro='%s'"%intro)
            mids = ",".join(mid)
            suffix = (" WHERE userId = '%s'" % userId)
            sql_str = prefix + mids + suffix
            print(sql_str)
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            print('Insert USR operation error')
            raise
        finally:
            cur.close()
            con.close()


    def query_person(self, userId):
        sql_str = ("SELECT userId,nickname,gender,intro"
                + " FROM usr_info WHERE userId = '%s'" % userId)
        #"nickname": ,"gender": , "wechatID": , "details":
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
            print('Insert USR operation error')
            raise
        finally:
            cur.close()
            con.close()

    # def update_site(self, ):
    
    def query_site(self, site):
        siteId = site.getSiteId()
        sql_str = ("SELECT siteId, name, address, sportsType"
                + " FROM site_info WHERE siteId = '%s'" % siteId)
        #"nickname": ,"gender": , "wechatID": , "details":
        print(sql_str)
        con = self.connect_db()
        cur = con.cursor()
        cur.execute(sql_str)
        rows = cur.fetchall()
        cur.close()
        con.close()

        return rows
    
    def insert_match(self, userId, sportsType, sportsLocation, startTime, endTime):
        con = self.connect_db()
        cur = con.cursor()
        try:
            sql_str = ("INSERT INTO match_info (userId,SportsType,SportsLocation,StartTime,EndTime)" 
                        + " VALUES ('%s', '%s','%s','%s', '%s')" % (userId,sportsType,sportsLocation,startTime,endTime))
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
        sportsType, sportsLocation = query["sportsType"], query["sportsLocation"]
        if sportsType == None:
            condition = ("(SportsLocation = '%s')" % sportsType)
        else:
            condition = ("(SportsType = '%s' AND SportsLocation = '%s')" % (sportsType, sportsLocation))

        sql_str = "SELECT DISTINCT userId, StartTime, EndTime" + " FROM match_info WHERE " + condition
        # "(StartTime = '%s' OR EndTime = '%s')
        print(sql_str)
        con = self.connect_db()
        cur = con.cursor()
        cur.execute(sql_str)
        rows = cur.fetchall()
        cur.close()
        con.close()

        return rows

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

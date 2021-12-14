from json.encoder import JSONEncoder
from flask import Flask
from flask import request
from flask import render_template, redirect,url_for
from flask import jsonify
import json
import os
from service import personService, siteService
from factory import factory
from instance import *

app = Flask(__name__)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

class controller:
    def __init__(self, ip_address, port):
        self.siteService = siteService()
        self.personService = personService()
        self.factory = factory()
        self.ip_address = ip_address
        self.port = port

    def dispatch(self, msg):
        '''
            dispatch the message according to 'mark' value
        '''
        result = None
        if msg['mark'] == Message.login:
            openId = self.personService.queryOpenId(msg)
            print("openId: ", openId)
            result = self.personService.viewPersonInfo(openId)
            # print(tmp_result, type(tmp_result))
            if len(result) == 0:
                person = self.factory.generatePerson(openId)
                result = self.personService.addNewPerson(person)
        elif msg['mark'] == Message.updatePersonInfo:
            person = self.factory.generatePerson(msg)
            self.personService.updatePersonInfo(person)
            result = self.personService.viewPersonInfo(person.getOpenId())
        elif msg['mark'] == Message.siteSearch:
            #todo: count the person number of each site
            result = self.siteService.siteSearch(msg)
        elif msg['mark'] == Message.viewSitePersonList:
            result = self.personService.matchPersonList(msg)
        elif msg['mark'] == Message.viewPersonInfo:
            openId = msg['openId']
            result = self.personService.viewPersonInfo(openId)
        elif msg['mark'] == Message.viewMatchPersonList:
            result = self.personService.matchPersonList(msg)
            self.personService.insertMatchInfo(msg)

        return result
    
    def run(self):
        app.debug = True
        app.json_encoder = MyEncoder
        app.run(self.ip_address, self.port, threaded = False, processes=10)

@app.route('/',methods = ['GET'])
def recv_data():
    '''
        receive data and handle message
    '''
    recv_data = request.args
    print(recv_data)
    result = server.dispatch(recv_data)
    print(result, type(result))
    return jsonify(result)

if __name__ == "__main__":
    server = controller("10.209.102.112", 5001)
    server.run()
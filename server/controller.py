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

class controller():
    def __init__(self, ip_address, port):
        self.siteService = siteService()
        self.personService = personService()
        self.factory = factory()
        self.ip_address = ip_address
        self.port = port

    def handle_message(self, msg):
        '''
            handle the message according to 'mark' value
        '''
        result = None
        if msg['mark'] == Message.login:
        # if msg['mark'] == '0':
            person = self.factory.generatePerson(msg)
            result = self.personService.addNewPerson(person)
        elif msg['mark'] == Message.updatePersonInfo:
        # elif msg['mark'] == '1':
            person = self.factory.generatePerson(msg)
            result = self.personService.updatePersonInfo(person)
        elif msg['mark'] == Message.siteSearch:
        # elif msg['mark'] == '2':
            print(msg['mark'], type(msg['mark']), Message.siteSearch, type(Message.siteSearch))
            result = self.siteService.siteSearch(msg)
        elif msg['mark'] == Message.viewSiteInfo:
        # elif msg['mark'] == '3':
            result = self.personService.matchPersonList(msg)
        elif msg['mark'] == Message.viewPersonInfo:
        # elif msg['mark'] == '4':
            userId = msg['userId']
            result = self.personService.viewPersonInfo(userId)
        elif msg['mark'] == Message.matchSearch:
        # elif msg['mark'] == '5':
            site = self.factory.generateSite(msg)
            if not self.siteService.querySite(site):
                self.siteService.addNewSite(site)
            result = self.personService.matchPersonList(msg)

        return result
    
    def run(self):
        app.debug = True
        app.run(self.ip_address, self.port, threaded = False, processes=10)

# class controller():
#     def __init__(self, ip_address, port):
#         self.siteService = siteService()
#         self.personService = personService()
#         self.factory = factory()
#         self.ip_address = ip_address
#         self.port = port
    
#     @app.route('/',methods = ['GET'])
#     def recv_data(self):
#         '''
#             receive data and handle message
#         '''
#         recv_data = request.args
#         print(recv_data)
#         result = self.handle_message(recv_data)
#         print(result)
#         return jsonify(result)

#     def handle_message(self, msg):
#         '''
#             handle the message according to 'mark' value
#         '''
#         if msg['mark'] == Message.login:
#             person = self.factory.generatePerson(msg)
#             result = self.personService.addNewPerson(person)
#         elif msg['mark'] == Message.updatePersonInfo:
#             person = self.factory.generatePerson(msg)
#             result = self.personService.updatePersonInfo(person)
#         elif msg['mark'] == Message.siteSearch:
#             result = self.siteService.siteInfo(msg)
#         elif msg['mark'] == Message.viewSiteInfo:
#             result = self.personService.matchPersonList(msg)
#         elif msg['mark'] == Message.viewPersonInfo:
#             userId = msg['userId']
#             result = self.personService.viewPersonInfo(userId)
#         elif msg['mark'] == Message.matchSearch:
#             site = self.factory.generateSite(msg)
#             if not self.siteService.querySite(site):
#                 self.siteService.addNewSite(site)
#             result = self.personService.matchPersonList(msg)

#         return result
    
#     def run(self):
#         app.debug = True
#         app.run(self.ip_address, self.port, threaded = False, processes=10)
server = controller("10.209.102.112", 5001)

@app.route('/',methods = ['GET'])
def recv_data():
    '''
        receive data and handle message
    '''
    recv_data = request.args
    print(recv_data)
    result = server.handle_message(recv_data)
    #print(result)
    return jsonify(result)

if __name__ == "__main__":
    server.run()
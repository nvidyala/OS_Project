import os
import motor
from motor import MotorClient
#Tornado libraries
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application, asynchronous, removeslash
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import engine, Task, coroutine
import tornado.ioloop
import tornado.web

db = MotorClient()['ppa']

class LoginHandler(RequestHandler):
	@removeslash
	@coroutine
	def get(self):
		#username = self.get_aurgument('username')
		#password = self.get_aurgument('password')
		self.render('templates/login.html')


class SignUpHandler(RequestHandler):
	@coroutine
	def post(self):
		username = self.get_argument('username')
		password = self.get_argument('password')
		writeData = {'username':username,'password':password}
		db = self.settings['db']
		print(username)
		self.render('login.html')


class clientServer(RequestHandler):
	@removeslash
	def post(self):
		writeData = {}		

application = tornado.web.Application([(r'/login', LoginHandler),
	(r'/',LoginHandler)
	],db = db,debug=True)
 
#main init
if __name__ == "__main__":
	application = HTTPServer(application)
	application.listen(6969)
	tornado.ioloop.IOLoop.instance().start()
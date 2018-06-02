import flask_login
from flask import Flask,session,redirect,url_for,escape,request,render_template,make_response,jsonify
import gzpm_logger
import sys
import os
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
login_manager.init_app(app)

#获取logger实例
logger = gzpm_logger.get_logger(__name__)
logger.info("成功引用日志模块")
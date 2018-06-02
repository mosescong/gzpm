import os
import logging
from logging.handlers import RotatingFileHandler
import time
import sys


LOG_PATH = os.path.abspath(os.path.dirname(sys.argv[0])) + '/Logs/'
log_rq = time.strftime("%Y-%m-%d",time.localtime(time.time()))
log_name = LOG_PATH + 'AppLog' + log_rq + '.log'

def get_logger(name):
	i_logger=logging.getLogger(name)
	if os.path.exists(LOG_PATH):
		pass
	else:
		os.makedirs(LOG_PATH)
	'''print(os.getcwd()) # 获得当前工作目录
	print(os.path.abspath('.'))# 获得当前工作目录
	print(os.path.abspath('..'))  # 获得当前工作目录的父目录
	print(os.path.abspath(os.curdir))  # 获得当前工作目录
	print(os.path.abspath(os.path.dirname(sys.argv[0])))'''
	#指定logger输出格式
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	#文件日志
	file_handler = logging.FileHandler(log_name)
	file_handler.setFormatter(formatter)

	#控制台日志
	console_handler = logging.StreamHandler()
	#console_handler.setLevel(logging.INFO)
	console_handler.setFormatter(formatter)

	#为logger添加的日志处理器，加入设定的输出配置
	i_logger.addHandler(file_handler)
	i_logger.addHandler(console_handler)

	#指定日志最低的输出级别，默认为WARN级别
	i_logger.setLevel(logging.DEBUG)
	return i_logger

if __name__ == '__main__':
	logger=get_logger(__name__)
	logger.debug("test")


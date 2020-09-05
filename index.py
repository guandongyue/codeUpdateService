#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-09-05 16:05:06
# @Author  : Molsen (guandongyue@gmail.com)
# @Link    : http://www.guandongyue.com
# @Version : $Id$

from flask import Flask
import subprocess

app = Flask(__name__)

def updateCommand():
    return subprocess.check_output('cd /data/app/php/xxx && git pull',shell=True)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/update', methods = ['POST', 'GET'])
def update():
    return updateCommand()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
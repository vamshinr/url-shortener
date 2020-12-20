#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:13:59 2020

@author: vamshi_kiran
"""

import flask
from flask import Flask,request,jsonify,redirect
import re
import hashlib
import base64
app=Flask(__name__)
urls_dict = {}

@app.route('/')
def index():
    return flask.render_template('home.html')

def shortcode(url):
    global urls_dict
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
    base_URL = urls[0]
    attached_URL = url.replace(base_URL,"")
    if url not in urls_dict.values():
        temp_URL = base64.b64encode(hashlib.md5(attached_URL.encode()).digest()[-4:]).decode("utf-8").replace('=','').replace('/','').replace("+","")
        urls_dict[temp_URL]=url
    else:
        for key,value in urls_dict.items():
            if value == url:
                temp_URL = key
    return temp_URL
    
@app.route('/generate',methods=['POST'])
def result():
    text = request.form
    key,url=list(text.items())[0]
    shorturl = "https://url--shorten.herokuapp.com/"+shortcode(url)
    return flask.render_template('result.html',original_url=url,short_url=shorturl,redirect_url=urls_dict[shortcode(url)])

@app.route('/<short_url>')
def redirect_short_url(short_url):
    print(urls_dict)
    if short_url in urls_dict.keys():
        return redirect(urls_dict[short_url])
    
if __name__=="__main__":
    app.run(threaded=True)
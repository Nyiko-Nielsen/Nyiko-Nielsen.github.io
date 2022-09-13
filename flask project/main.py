# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:09:38 2022

@author: nymaswan2201
"""

from flask import Flask, render_template
app = Flask(__name__)
  
@app.route("/home")
def index():
   return render_template("index.html")
  
if __name__ == '__main__':
   app.run( )
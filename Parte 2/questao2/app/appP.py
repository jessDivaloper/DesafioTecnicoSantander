# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 00:32:29 2021

@author: JESS
"""

from flask import Flask, render_template
#import os

app = Flask(__name__)

@app.route('/')
def raiz():
    return render_template('index.html') 

if __name__ == '__main__':

    app.run()
    
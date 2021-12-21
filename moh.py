from flask import *

import os

app = Flask(__name__)

def get_files():
 return [ "<a href='/{}'>{}</a>".format(entry.name,entry.name) for entry in os.scandir('/data/data/com.termux/files/home/SmartDeliverySystems_Exploit') if entry.is_file() and entry.name.endswith('.json') ]

@app.route('/<file>.json', methods = ['GET'])
def downloads(file):
 return send_file("{}.json".format(file), as_attachment=True)
 

@app.route('/', methods = ['GET'])
def home():
 return "<br>".join(get_files())
 
if __name__ == '__main__':
   app.run()

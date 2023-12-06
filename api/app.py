from flask import Flask, render_template,request
import json,urllib.request
import random
app = Flask(__name__, static_url_path='/static')
Rr=-100
Rr01=-100
@app.route('/', methods=('GET', 'POST'))
def index():
    global Rr
    global Rr01

    Qu=''
    As=''    
    url ="https://ccvs1209.vercel.app/static/song.json"    
    
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    if request.method=='POST':
        btQu=request.values.get('myQu')
        btAns=request.values.get('myAns')        
        if btQu=='myQu':
           Rr=random.randint(0,89)
           Rr01=111
           Qu=output[Rr]['name']
           As=output[Rr]['d1']
           return render_template('index.html',Qu=Qu,As=As,Rr01=Rr01)            
        if btAns=='myAns':
            Rr01=100
            Qu=output[Rr]['name']
            As=output[Rr]['d1']             
            return render_template('index.html',Qu=Qu,As=As,Rr01=Rr01)   

    return render_template('index.html',Qu=Qu,As=As,Rr01=Rr01)

if __name__ == '__main__':
    app.run()

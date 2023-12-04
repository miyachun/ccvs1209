from flask import Flask, render_template,request
import json,urllib.request
import random
app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=('GET', 'POST'))
def index():
    
    f1=[]
    f2=[]    
    url ="https://ccvs1209.vercel.app/static/sample.json"
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    if request.method=='POST':
        btA=request.values.get('myA')
        btB=request.values.get('myB')
        if btA=='myA':
           f1.clear()
           f2.clear()
           Rr=random.randrange(0, 89, 1)
           f1.append(output[Rr]['name'])
           f2.append(output[Rr]['d1'])
        if btB=='myB':
            f1.clear()
            f2.clear()
            return render_template('index.html',dF1=f1,dF2=f2)    
    return render_template('index.html',dF1=f1,dF2=f2)

if __name__ == '__main__':
    app.run()

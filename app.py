from flask import Flask,render_template,abort,request,redirect
import pyrebase
app = Flask(__name__)

config={
    "apiKey": "AIzaSyBdpHdj2iFUP8HBgoIyPJHV5AtTm2gEdrg",
    "authDomain": "dassar-2f18c.firebaseapp.com",
    "databaseURL": "https://dassar-2f18c-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "dassar-2f18c",
    "storageBucket": "dassar-2f18c.appspot.com",
    "messagingSenderId": "606850049804",
    "appId": "1:606850049804:web:e5aac4f298024b23e08b29"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route('/')
def index():
    h1=0;f1=0
    h2=0;f2=0
    h3=0;f3=0
    h4=0;f4=0

    datalevel1 = db.child('level1').get().val()
    for r in datalevel1 :
        if datalevel1[r]['sex']=='h':
            h1=h1+1
        else:
            f1+=1

    datalevel2 = db.child('level2').get().val()
    for r in datalevel2 :
        if datalevel2[r]['sex']=='h':
            h2=h2+1
        else:
            f2+=1

    datalevel3 = db.child('level3').get().val()
    for r in datalevel3 :
        if datalevel3[r]['sex']=='h':
            h3+=1
        else:
            f3+=1

    datalevel4 = db.child('level4').get().val()
    for r in datalevel4 :
        if datalevel4[r]['sex']=='h':
            h4=h4+1
        else:
            f4+=1

    count = {"l1":[h1,f1],"l2":[h2,f2],"l3":[h3,f3],"l4":[h4,f4],}
    #db.child('level2').push({"fname":"Meriem","adresse":"Casablanca","lname":"errkhis","bday":"10.03.2012","id":3,"sex":"f","status":"abandonner"})
    return render_template('index.html',count=count)

@app.route('/classes/<int:id>')
def classes(id):
    if id == 1:
        data = db.child('level1').get().val()
    if id == 2:
        data = db.child('level2').get().val()
    if id == 3:
        data = db.child('level3').get().val()
    if id == 4:
        data = db.child('level4').get().val()
    return render_template('classe.html',d = data,id=id)
    

@app.route('/add/level<int:id>',methods=['POST','GET'])
def add(id):
    if id>4 or id==0:
        abort(404)
    return render_template('add.html',id=id)

@app.route('/sub/<int:id>',methods=['POST'])
def sub(id):
    fnm = request.form.get('name')
    addr = request.form.get('addr')
    lnm = request.form.get('pnom')
    sx = request.form.get('sx')
    dn = request.form.get('dn')
    name = request.form.get('name')
    st = "encore"

    pdata = {"adresse":addr,"bday":dn,"fname":fnm,"lname":lnm,"sex":sx,"status":st,"id":10}
    childname = "level"+str(id)
    db.child(childname).push(pdata)
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)

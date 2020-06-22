from flask import Flask, render_template, request, redirect
import json
from database.database import Database

app = Flask('__name__', static_folder='static', static_url_path='/static')
application = app

@app.route('/', methods=['GET','POST'])
def dashboard():
    
    db = Database()
    columns = ["Serial #", "Item", "Location", "Amount","Putt / Pull / Delete"]
    
    try:
        if(request.form['search'] == "1"):
            name = request.form['name']
            
            if(name == ""):
                items = db.getAllItems()
            else:
                items = db.getByName(name)
        else:
            items = db.getAllItems()
            
    except:
        items = db.getAllItems()
        
    return render_template("dashboard.html",columns = columns,table_data=items)

@app.route('/update', methods=['GET', 'POST'])
def update_page():
    if request.method == 'POST':
        serial = request.form['secret']
        db = Database()
        thing = db.getBySerial(serial)

    return render_template("update.html", item = thing)
    
@app.route('/remove', methods=['POST'])
def remove_item():
    if request.method == 'POST':
        serial = request.form['serial']
        db = Database()
        db.deleteItem(serial)
        
    return redirect("/warehouse")
    
@app.route('/dashboard', methods=['GET', 'POST'])
def updated_dashboard():
    if request.method == 'POST':
        serial = request.form['serial']
        choice = request.form['choice']
        amt = int(request.form['amount'])
    
        if(choice == "pull") :
            amt *= -1
            #Add check for going negative, possible database side...
        
        db = Database()
        db.changeItemAmount(serial, amt)
        
    columns = ["Serial #", "Item", "Location", "Amount","Putt / Pull"]
    items = db.getAllItems()
    
    return redirect("/warehouse")
    
@app.route('/addnew', methods=['POST', 'GET'])
def add_new():
    
    return render_template("addnew.html")
    
@app.route('/itemsubmit', methods=['POST'])
def submit():
    
    #Add some server side validation
    
    serial = request.form['serial']
    name = request.form['name']
    location = request.form['location']
    amount = request.form['amount']
    
    db = Database()
    db.addItem(serial, name, location, amount)
    
    return redirect("/warehouse")
    
@app.route('/about')
def about():
    
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True) #Set to local host currently


from flask import Flask, render_template, request, redirect
import json
from database.database import Database
from database.database_tools import db_tool
from profanityfilter import ProfanityFilter

app = Flask('__name__', static_folder='static', static_url_path='/static')

#This is the dashboard page of the program
@app.route('/', methods=['GET','POST'])
def dashboard():

    db = Database() #Represents the database holding items
    columns = ["Serial #", "Item", "Location", "Amount","Putt / Pull / Delete"]
    
    #This try-except is used to determine if there was a search submitted by the user
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

#This loads in the data of the chosen item and passes the info to the html document
@app.route('/update', methods=['GET', 'POST'])
def update_page():
    if request.method == 'POST':
        serial = request.form['secret']
        db = Database()
        thing = db.getBySerial(serial)

    return render_template("update.html", item = thing)
    
#If it has been chosen to delete the item, this method is called, and then the user is redirected to the dashboard
@app.route('/remove', methods=['POST'])
def remove_item():
    if request.method == 'POST':
        serial = request.form['serial']
        db = Database()
        db.deleteItem(serial)
        
    return redirect("/warehouse")
    
#This updates the item after the user presses submit, and then redirects them to the dashboard
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
    
    return redirect("/warehouse")

#Simply loads the addnew html file
@app.route('/addnew', methods=['POST', 'GET'])
def add_new():
    
    return render_template("addnew.html")
   
#After submitting the new item, this method is called.
#Then the user is redirected to the dashboard 
@app.route('/itemsubmit', methods=['POST'])
def submit():
    
    pf = ProfanityFilter(no_word_boundaries = True)
    serial = request.form['serial']
    name = request.form['name']
    location = request.form['location']
    amount = request.form['amount']
    
    #Since this is an open text field accessible on a public website,
    #some form of profanity check is needed
    if pf.is_profane(name):
        return redirect("/warehouse")
    
    else:
        db = Database()
        db.addItem(serial, name, location, amount)
        return redirect("/warehouse")
    
#Simply loads the about html file
@app.route('/about')
def about():
    
    return render_template("about.html")
    
#Semi-obscure route that I have a cron job set up for my RaspberryPi
#Flushes out the database and adds back all original entries
#Resests once per day at 2am 
@app.route('/resetdatabase0200am')
def reset():
    
    initializer = db_tool()
    initializer.deleteAll()
    initializer.addItems()
    
    return "Okay"

#How the flask app starts itself up
if __name__ == '__main__':
    app.run(debug=True)


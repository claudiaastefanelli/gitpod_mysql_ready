from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/units')
def unitList():
    mycursor.execute("SELECT * FROM Clash_Unit")
    myresult= mycursor.fetchall()
    return render_template('clash_units.html', units=myresult)
    
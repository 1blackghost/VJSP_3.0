#Main Website Script
from EMS import emails
from Utilities import Generate_Random_String
from DBMS import Deletion,Updation,Manger
from flask import *

app=Flask(__name__)
get_key=Generate_Random_String.generate(20)
app.secret_key=str(get_key)

#routes
@app.route("/")
def root():
    return "Hello from flask"


with app.app_context():
    from authen import *
    from views import *
if __name__=="__main__":
    app.run(debug=True)





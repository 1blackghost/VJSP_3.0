#Handles views of the users.
from main import app

@app.route("/aboutus")
def aboutus():
    return "Its about us page"
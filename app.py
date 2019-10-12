from flask import url_for,redirect,Flask,render_template
import Service
import mongoService
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/bookdemo")
def bookdemo():
    return url_for('about')
#def hello():
#    return "hello world!!"
@app.route("/t1")
def hello1():
    return "t1"
@app.route("/sql")
def des_sql():
    return (str(Service.Sql_db().describe()))
@app.route("/bookinfo")
def book_list():
    return(str(mongoService.Mg().get_all()))
        
@app.route("/bookinfo/<asin>")
def show_book(asin):
    return(str(mongoService.Mg().get_all_info(asin)))
if __name__=="__main__":
    app.run(debug=True)


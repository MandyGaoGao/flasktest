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
@app.route("/bookindex/<page_num>")
def book_list_page(page_num):
    page_num=int(page_num)
    ls=mongoService.Mg().get_all()
    total=len(ls)//20
    if page_num==total:
        return(str(ls[page_num*20:]))
    elif page_num>total:
        return("no more books!")
    else:
        return(str(ls[page_num*20:(page_num+1)*20])) 

@app.route("/bookinfo/<asin>")
def show_book(asin):
    book_info=mongoService.Mg().get_all_info(asin)
    return(render_template("info.html",book_info=book_info))
@app.route("/dashboard")
def dashboard():
    return(render_template("dashboard.html"))
@app.route("/login")
def login():
    return(render_template("login.html"))

@app.route("/registration")
def registration():
    return(render_template("registration.html"))
@app.route("/search")
def search():
    return(render_template("search.html"))



if __name__=="__main__":
    app.run(debug=True)


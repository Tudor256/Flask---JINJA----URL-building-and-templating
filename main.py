from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


gender_URL='https://api.genderize.io'
age_URL='https://api.agify.io'


parameters={'name': 'Joe',}
resp = requests.get(gender_URL, params=parameters)
resp.raise_for_status()
data_gender=resp.json()['gender']
print(data_gender)



@app.route('/')
def home():
    random_number=random.randint(1,10)
    today = datetime.date.today()
    current_year = today.year
    return render_template('index.html', num=random_number, current_year=current_year)  #!!!you can add argumnets here (ex.: num) which you can use in the html code



#<name> is variable and can be changed from path 
@app.route("/guess/<name>")
def greet(name):

    #import api's below to generate the gender and age variables from api
    parameters={'name': name,}
    resp = requests.get(gender_URL, params=parameters)
    resp.raise_for_status()
    gender=resp.json()['gender']

    
    respo = requests.get(age_URL, params=parameters)
    respo.raise_for_status()
    age=respo.json()['age']

    #store the name,  gender and age variables for later re-use in html
    return render_template('guess.html', name=name, gender=gender, age=age)



@app.route("/blog/<num>")
def get_blog(num):
    blog_URL='https://api.npoint.io/c790b4d5cab58020d391'
    print(num)
    resp1 = requests.get(blog_URL)
    resp1.raise_for_status()
    all_posts=resp1.json()
    return render_template('blog.html', posts=all_posts)



app.run(debug=True)



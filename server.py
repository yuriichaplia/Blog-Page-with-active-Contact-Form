import smtplib
import requests
from os import environ
from flask import Flask
from flask import request
from dotenv import load_dotenv
from flask import render_template

app = Flask(__name__)

load_dotenv()
EMAIL = environ["MY_EMAIL"]
TO_EMAIL = environ["TO_EMAIL"]
PASSWORD = environ["MY_PASSWORD"]

blog_data = requests.get(url="https://api.npoint.io/85adf096d1c1ab93961b")
blog_data.raise_for_status()
blog_data = blog_data.json()

@app.route('/')
def home_page():
    return render_template('index.html', data = blog_data)

@app.route('/about')
def about_page():
    return render_template('about.html')

def send_message(name, email, number, message):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=TO_EMAIL,
                            msg=f'Subject: Project\n\n Name: {name}\n Email: {email}\n Phone number: {number}\n '
                                f'Message: {message}')

@app.route('/contact', methods=["POST", "GET"])
def contact_page():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        number = request.form["phone"]
        message = request.form["message"]

        send_message(name, email, number, message)
        return render_template('contact.html', msg_sent=True)
    else:
        return render_template('contact.html', msg_sent=False)

@app.route('/post/<number>')
def post_page(number):
    title = blog_data[int(number) - 1]['title']
    subtitle = blog_data[int(number) - 1]['subtitle']
    date = blog_data[int(number) - 1]['date']
    body = blog_data[int(number) - 1]['body']
    return render_template('post.html',
                           title=title, subtitle=subtitle, date=date, body=body)

if __name__ == "__main__":
    app.run(debug=True)
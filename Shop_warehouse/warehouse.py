"""Server flask to host endpoint connection to database and client app"""
from flask import Flask
import requests
from requests.exceptions import HTTPError
from json import JSONEncoder
import os
from database import Database
import logging
from  flask import render_template, flash, redirect, url_for, request


logging.basicConfig(filename='log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.secret_key = os.environ['secret_key']
database = Database()

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    data = database.get_all_books()
    return render_template('admin.html', data_book = data)

@app.route("/add_author", methods=['GET', 'POST'])
def add_author():  
    if request.method == 'POST':
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            if first_name == "" or last_name == "" :
                message = f'Te pola nie mogą być puste'
        except ValueError as e:
            logging.error(e)
            message = e
        
        message = database.add_author(first_name, last_name)
        flash(f'{message}')
        return redirect('/admin')
    return render_template('add_author.html') 


if __name__ == '__main__':
    app.run(debug=True,port=8080)
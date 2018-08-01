import datetime
import os
from threading import Thread

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_sslify import SSLify

from inbound_upload import sheets

application = Flask(__name__)

# FORCES REROUTE TO HTTPS
# REMOVE FOR LOCAL DEV
sslify = SSLify(application)


@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/about')
def services():
    return render_template('about.html')


@application.route('/value', methods=['POST', 'GET'])
def value():
    if request.method == 'GET':
        return render_template('value.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        car = request.form['car']
        location = request.form['location']
        service = request.form['service']
        date = request.form['date']

        if name and email and phone and car and location and date:
            package = [datetime.datetime.now().strftime('%M-%d-%Y %H:%M:%S'), name, email, phone, car, location,
                       service,
                       date]
            value_thr = Thread(target=sheets, args=[package])
            value_thr.start()
            return jsonify(
                {'name': "Thanks " + name + ", we'll confirm your valuation shortly!"})

        return jsonify(
            {
                'error': "Double check all the inputs are filled out"})


@application.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        if name and email and phone and message:
            ## FIGURE OUT EMAIL FORM

            return jsonify(
                {'response': "Thanks " + name.split()[0] + ", we'll get back to you ASAP"})

        return jsonify(
            {'error': "Some fields seem to be missing"})


@application.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    car = request.form['car']
    location = request.form['location']
    service = request.form['service']
    date = request.form['date']

    if name and email and phone and car and location and date:
        package = [datetime.datetime.now().strftime('%M-%d-%Y %H:%M:%S'), name, email, phone, car, location, service,
                   date]
        thr = Thread(target=sheets, args=[package])
        thr.start()
        return jsonify(
            {'name': "Thanks for your submission " + name + ", we'll reach out to you at " + email + " shortly."})

    return jsonify(
        {
            'error': "Check that all the fields are filled out correctly!"})


@application.errorhandler(500)
def error_500(e):
    return render_template('error.html', value='500', description=e)


@application.errorhandler(404)
def error_404(e):
    return render_template('error.html', value='404', description=e)


@application.errorhandler(405)
def error_405(e):
    return render_template('error.html', value='405', description=e)


if __name__ == '__main__':
    application.run()

import datetime
from threading import Thread

from flask import Flask, render_template, request, jsonify
from flask_sslify import SSLify

from inbound_upload import sheets
app = Flask(__name__)

# FORCE SSL
# REMOVE FOR LOCAL DEV
sslify = SSLify(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def services():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/value', methods=['POST', 'GET'])
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


@app.route('/process', methods=['POST'])
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
            {'name': "Thanks " + name + ", we've sent you a confirmation email at " + email + "."})

    return jsonify(
        {
            'error': "Check that all the fields are filled out correctly!"})


@app.route('/sitemap.xml')
def sitemap():
    return app.send_static_file('sitemap.xml')


@app.errorhandler(500)
def error_500(e):
    return render_template('error.html', value='500', description=e)


@app.errorhandler(404)
def error_404(e):
    return render_template('error.html', value='404', description=e)


@app.errorhandler(405)
def error_405(e):
    return render_template('error.html', value='405', description=e)


if __name__ == '__main__':
    app.run()

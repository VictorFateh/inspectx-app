from flask import Flask, render_template, request, jsonify, send_from_directory
from inbound_upload import sheets
from threading import Thread
import datetime
import os

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def services():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
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


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    car = request.form['car']
    location = request.form['location']
    service = request.form['service']
    date = request.form['date']

    if name and email and phone and car and location and service and date:
        package = [datetime.datetime.now().strftime('%M-%d-%Y %H:%M:%S'), name, email, phone, car, location, service,
                   date]
        thr = Thread(target=sheets, args=[package])
        thr.start()
        return jsonify(
            {'name': "Thanks for your submission " + name + ", we'll reach out to you at " + email + " shortly."})

    return jsonify(
        {
            'error': "Looks like there's a problem with some of fields. Double check that they're filled out correctly!"})


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
    app.run(debug=True, TEMPLATES_AUTO_RELOAD=True)
    # FOR EC2
    # app.run(host="0.0.0.0", port='80')

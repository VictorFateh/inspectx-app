from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/email', methods=['POST'])
def email():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['car']

    if name and email and phone and message:
        return jsonify(
            {'name': "Thanks " + name + ", we'll get back to you ASAP"})

    return jsonify(
        {
            'error': "Some fields seem to be missing"})


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    car = request.form['car']
    location = request.form['location']
    date = request.form['date']

    if name and email and phone and car and location and date:
        # GOOGLE SHEETS OR FIREBASE LOGIC HERE

        return jsonify(
            {'name': "Thanks for your submission " + name + ", we'll reach out to you at " + email + " shortly."})

    return jsonify(
        {
            'error': "Oops, looks like there's a problem with some of fields. Double check that they're filled out correctly!"})


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
    app.run(debug=True)

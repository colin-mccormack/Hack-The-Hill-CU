from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'zbnlfzdgrzhsrd'



@app.route('/')
def home():
    return render_template('index.html', msg='')


@app.route('/data/', methods=['GET', 'POST'])
def data():
    msg = 'Error'

    if request.method == 'POST':
        # Create variables for easy access
        fname = request.form['fname']
        lname = request.form['lname']
        res_code = request.form['res_code']
        # connect to db
        # send params to db
        # get return data
        # set msg to return data
        session['loggedin'] = True
        msg = fname + " : " + lname + " : " + res_code
        return render_template('results.html', results=msg)

    return redirect(url_for('/'))

@app.route('/results')
def results():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        results = ''
        return render_template('results.html', results=results)
    # User is not loggedin redirect to login page
    return redirect(url_for('/'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
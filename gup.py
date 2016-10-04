from flask import Flask, render_template, request
import log

app = Flask(__name__)

@app.route("/")
def temp():
    print"\n\n\n"
    print "this the apperrino"
    print app
    d = request.form
    if 'user' in d.keys():
        log.add(d['user'], d['pass'])
        return render_template("input.html", stuff = "SUCCESS!")
    else: return render_template("input.html", stuff = "")

@app.route("/auth", methods=['POST'])
def author():
    print"\n\n\n"
    print "this the apperrino"
    print app
    if request.form['usr'] == "fortune" and request.form['pwd'] == "pqss1234":
        return render_template("success.html")
    else: return render_template("failure.html")

if __name__ == "__main__":
    app.debug = True
    app.run()

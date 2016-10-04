from flask import Flask, render_template, request
import log

app = Flask(__name__)

@app.route("/")
def temp():
    print"\n\n\n"
    print "this the apperrino"
    print app
    d = request.form
    return render_template("input.html", stuff = log.add(d['user'], d['pass']))

@app.route("/auth", methods=['POST'])
def author():
    print"\n\n\n"
    print "this the apperrino"
    print app
    if log.check(request.form['usr'], request.form['pwd']):
        return render_template("success.html")
    else: return render_template("input.html", stuff = "ACC NOT FOUND.")

if __name__ == "__main__":
    app.debug = True
    app.run()

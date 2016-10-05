from flask import Flask, render_template, request
import util.log

app = Flask(__name__)

@app.route("/")
def temp():
    print"\n\n\n"
    print "this the apperrino"
    print app
    d = request.form
    if 'user' in d.keys():
        return render_template("input.html", stuff = log.add(d['user'], d['pass']))
    else: return render_template("input.html", stuff = "")

@app.route("/auth", methods=['POST'])
def author():
    print"\n\n\n"
    print "this the apperrino"
    print app
    if log.check(request.form['usr'], request.form['pwd']):
        return render_template("input.html", stuff = "youer in. good jab.")
    else: return render_template("input.html", stuff = "ACC NOT FOUND.")

if __name__ == "__main__":
    app.debug = True
    app.run()

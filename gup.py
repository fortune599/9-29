from flask import Flask, render_template, request, redirect, session, url_for
import util.log, os

app = Flask(__name__)

app.secret_key = os.urandom(12)

@app.route("/")
def temp():
    print"\n\n\n"
    print "this the apperrino"
    print app
    if 'username' in session:
        return render_template("in.html", junk = session['username'])
    return render_template("input.html", stuff = "")

@app.route("/auth", methods=['POST'])
def author():
    print"\n\n\n"
    print "this the apperrino"
    print app
    d = request.form
    if 'user' in d.keys():
        return render_template("input.html", stuff = util.log.add(d['user'], d['pass']))
    if 'usr' in d.keys():
        if util.log.check(request.form['usr'], request.form['pwd']):
            session['username'] = request.form['usr']
            return redirect(url_for("temp"))
        else: return render_template("input.html", stuff = "ACC NOT FOUND.")
    else: return redirect(url_for("temp"))

@app.route("/jacobo")
def js():
    return redirect("http://xkcd.com")

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect(url_for("temp"))

if __name__ == "__main__":
    app.debug = True
    app.run()

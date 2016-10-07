from flask import Flask, render_template, request, redirect
import util.log

app = Flask(__name__)

@app.route("/")
def temp():
    print"\n\n\n"
    print "this the apperrino"
    print app
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
            return render_template("input.html", stuff = "youer in. good jab.")
        else: return render_template("input.html", stuff = "ACC NOT FOUND.")
    else: return redirect(url_for("/"))

@app.route("/jacobo")
def js():
    return redirect("http://xkcd.com")

if __name__ == "__main__":
    app.debug = True
    app.run()

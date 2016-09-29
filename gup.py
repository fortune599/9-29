from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def temp():
    print"\n\n\n"
    print "this the apperrino"
    print app
    print request.args
    return render_template("input.html")

@app.route("/auth", methods=['POST'])
def author():
    print"\n\n\n"
    print "this the apperrino"
    print app
    if request.form['usr'] == "fortune" and request.form['pwd'] == "pqss1234":
        return "KOAAAAAAAAA"
    else: return "no"

if __name__ == "__main__":
    app.debug = True
    app.run()

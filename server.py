from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def checkerboard():
    return render_template("index.html", across = 8, down = 8)

@app.route('/4')
def checkerboard():
    return render_template("four.html", across = 8, down = 4)

@app.route('/6/12')
def checkerboard():
    return render_template("xy.html", across = 6, down = 12)

if __name__=="__main__":
    app.run(debug=True)
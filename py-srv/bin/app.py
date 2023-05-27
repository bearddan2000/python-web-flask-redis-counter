from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)

redis = Redis(host="redis")

@app.route("/")
def hello():
    title = 'Python Flask Redis MVC Example'
    visits = redis.incr('counter')
    return render_template("index.html", title=title, visits=visits)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

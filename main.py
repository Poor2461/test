import flask

web=flask.Flask(__name__)

@web.route("/")
def main_page():
    return flask.render_template("home_page.html")

if __name__=="__main__":
  web.run(debug=True)

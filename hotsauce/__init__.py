from flask import Flask, render_template

app = Flask(__name__)

# index page


@app.route('/')
def index():
    try:
        return render_template("index.html", title="HotSauce")
    except Exception as e:
        return str(e)


@app.route('/about/')
def about():
    try:
        return render_template("about.html", title="About")
    except Exception as e:
        return str(e)


@app.route('/hotsauces/')
def hotsauces():
    try:
        return render_template("hotsauces.html", title="Hot Sauces")
    except Exception as e:
        return str(e)


@app.route('/brands/')
def brands():
    try:
        return render_template("brands.html", title="Brands")
    except Exception as e:
        return str(e)


@app.route('/peppers/')
def peppers():
    try:
        return render_template("peppers.html", title="Peppers")
    except Exception as e:
        return str(e)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="404 oops!")


if __name__ == "__main__":
    app.run(debug=True)

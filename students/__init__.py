from flask import Flask

from students import controllers


def init_app(app: Flask):
    app.add_url_rule(rule="/students",
                     view_func=controllers.index,
                     methods=["GET", "POST"])

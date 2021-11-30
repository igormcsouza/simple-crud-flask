from flask import Flask

from students import controllers


def init_app(app: Flask):
    app.add_url_rule(rule="/students",
                     view_func=controllers.index,
                     methods=["GET", "POST"])

    app.add_url_rule(rule="/students/<string:id>",
                     view_func=controllers.manage_single_student,
                     methods=["GET", "PUT", "DELETE"])

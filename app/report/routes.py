"""
Routes for rota report blueprint.
"""

from flask import render_template

from app.report import BP


@BP.route('/report')
def index():
    """
    Rota report form.

    :return: A form.
    :rtype: html
    """
    user = {'username': 'Nick'}
    return render_template('rota_report', title='Rota Report', user=user)

"""
Routes for rota report blueprint.
"""

import datetime

from flask import render_template

from app.report import BP


@BP.route('/report')
def index():
    """
    Rota report.

    :return: A report.
    :rtype: html
    """

    # Mock variables.
    member = {
        'name': 'Nick Taylor'
    }
    visit = {
        'no': 1,
        'date': datetime.date.today(),
        'start_time': datetime.time(12, 0, 0),
        'end_time': datetime.time(16, 0, 0),
        'manager': 'John Smith',
        'date_shift_handover': datetime.date.today(),
        'no_irc_detainees': 78
    }
    acdts = [
        {
            'name': "Dave",
            'nationality': "English",
            'room_no': "15A",
            'obs': "2 obs per day",
            'comments': "He is OK"
        },
        {
            'name': "James",
            'nationality': "Welsh",
            'room_no': "18D",
            'obs': "5 obs per day, 1 cons per day.",
            'comments': "He is not OK"
        },
    ]

    return render_template('rota_report.html', member=member, visit=visit,
                           acdts=acdts)

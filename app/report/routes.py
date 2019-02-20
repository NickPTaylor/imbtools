"""
Routes for report blueprint.
"""

import datetime

from flask import render_template, flash, redirect, url_for

from app.report import BP
from app.report.forms import ReportForm

@BP.route('/compose', methods=['GET', 'POST'])
def compose_report():
    """
    Compose rota report.

    :return: A composed submission.
    :rtype: html
    """
    form = ReportForm()
    if form.validate_on_submit():
        flash('Report created')
        return redirect(url_for('report.view_report'))
    return render_template('compose_report.html', form=form)


@BP.route('/view')
def view_report():
    """
    View rota report.

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

    return render_template('view_report.html', member=member, visit=visit,
                           acdts=acdts)

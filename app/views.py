from app import app, db
from app.forms import NewJobForm
from app.models import Job
from flask import flash, redirect, render_template, url_for


@app.route('/list')
def list():
    return render_template('list.html', title='List Reports')


@app.route('/')
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = NewJobForm()

    if form.validate_on_submit():
        j = Job(job_name=form.job_name,
                email=form.email,
                infill=form.infill,
                shells=form.shells,
                layer_height=form.layer_height,
                temperature=form.temperature,
                extrude_speed=form.extrude_speed,
                print_speed=form.print_speed)
        db.session.add(j)
        db.session.commit()
        flash('Report successfully submitted!')
        return redirect(url_for('submit'))

    return render_template('submit.html', title='Submit Report', form=form)
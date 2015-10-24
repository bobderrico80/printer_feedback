from app import app, db
from app.forms import NewJobForm
from app.models import Job
from flask import flash, redirect, render_template, url_for


@app.route('/view')
def view():
    jobs = Job.query.all()
    return render_template('view.html', title='View Reports', jobs=jobs)


@app.route('/')
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = NewJobForm()

    if form.validate_on_submit():
        j = Job(job_name=form.job_name.data,
                email=form.email.data,
                infill=form.infill.data,
                shells=form.shells.data,
                layer_height=form.layer_height.data,
                temperature=form.temperature.data,
                extrude_speed=form.extrude_speed.data,
                print_speed=form.print_speed.data)
        db.session.add(j)
        db.session.commit()
        flash('Report successfully submitted!')
        return redirect(url_for('submit'))

    return render_template('submit.html', title='Submit Report', form=form)
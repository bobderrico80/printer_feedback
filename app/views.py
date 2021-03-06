from app import app, db
from app.forms import NewJobForm
from app.models import Job
from flask import flash, redirect, render_template, request, make_response, url_for
from sqlalchemy.exc import IntegrityError


@app.route('/view')
def view():
    if 'p' in request.args:
        page = int(request.args['p'])
    else:
        page = 1

    jobs = Job.query.order_by(Job.job_name).paginate(page, 10)
    return render_template('view.html', title='View Reports', jobs=jobs)


@app.route('/')
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = NewJobForm()

    if form.validate_on_submit():
        if form.stl_file.data:
            stl_data = request.files[form.stl_file.name].read()
        else:
            stl_data = None
        j = Job(job_name=form.job_name.data,
                email=form.email.data,
                infill=form.infill.data,
                shells=form.shells.data,
                layer_height=form.layer_height.data,
                temperature=form.temperature.data,
                extrude_speed=form.extrude_speed.data,
                print_speed=form.print_speed.data,
                stl_file=stl_data)
        db.session.add(j)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('Sorry, there\'s already a job named {}'.format(j.job_name))
        else:
            flash('Report successfully saved!')
            return redirect(url_for('submit'))

    return render_template('edit.html',
                           title='Submit Report',
                           form=form,
                           form_context = 'add',
                           button_text='Submit Report')

@app.route('/edit/<int:job_id>', methods=['GET', 'POST'])
def edit(job_id):
    form = NewJobForm()
    job = Job.query.filter_by(id=job_id).first()

    if form.validate_on_submit():
        if form.validate_on_submit():
            if form.stl_file.data:
                stl_data = request.files[form.stl_file.name].read()
            else:
                stl_data = job.stl_file
        job = Job.query.filter_by(id=job_id).first()
        job.job_name = form.job_name.data
        job.email = form.email.data
        job.infill = form.infill.data
        job.shells = form.shells.data
        job.layer_height = form.layer_height.data
        job.temperature = form.temperature.data
        job.extrude_speed = form.extrude_speed.data
        job.print_speed = form.print_speed.data
        job.stl_file = stl_data

        db.session.add(job)
        db.session.commit()
        flash('Report successfully updated!')
        return redirect(url_for('view'))

    form.job_name.data = job.job_name
    form.email.data = job.email
    form.infill.data = job.infill
    form.shells.data = job.shells
    form.layer_height.data = job.layer_height
    form.temperature.data = job.temperature
    form.extrude_speed.data = job.extrude_speed
    form.print_speed.data = job.print_speed

    return render_template('edit.html',
                           title='Edit Report',
                           job_id=job.id,
                           form=form,
                           form_context='edit',
                           button_text='Save Changes')

@app.route('/delete/<int:job_id>')
def delete(job_id):
    job = Job.query.filter_by(id=job_id).first()

    db.session.delete(job)
    db.session.commit()
    flash('Report deleted')
    return redirect(url_for('view'))

@app.route('/download/<int:job_id>')
def download(job_id):
    job = Job.query.filter_by(id=job_id).first()
    file_data = job.stl_file
    response = make_response(file_data)
    response.headers['Content-Disposition'] = 'attachment; filename=job{}.atl'.format(job_id)
    return response

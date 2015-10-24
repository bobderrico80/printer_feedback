from app import db


class Job(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    job_name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    infill = db.Column(db.Integer(), nullable=False)
    shells = db.Column(db.Integer(), nullable=False)
    layer_height = db.Column(db.Numeric(), nullable=False)
    temperature = db.Column(db.Numeric(), nullable=False)
    extrude_speed = db.Column(db.String(16), nullable=False)
    print_speed = db.Column(db.String(16), nullable=False)

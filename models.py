from app import alba_stv_db as db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
	prenom = db.Column(db.String(50), nullable=False)
	nom = db.Column(db.String(50), nullable=False)
	classe = db.Column(db.String(50), nullable=False)
	self_1 = db.Column(db.String(50), nullable=False)
	self_2 = db.Column(db.String(50), nullable=False)
	self_3 = db.Column(db.String(50), nullable=False)
	self_4 = db.Column(db.String(50), nullable=False)
	self_5 = db.Column(db.String(50), nullable=False)
	self_6 = db.Column(db.String(50), nullable=False)
	other_1 = db.Column(db.String(50), nullable=False)
	other_2 = db.Column(db.String(50), nullable=False)
	other_3 = db.Column(db.String(50), nullable=False)
	other_4 = db.Column(db.String(50), nullable=False)
	other_5 = db.Column(db.String(50), nullable=False)
	other_6 = db.Column(db.String(50), nullable=False)
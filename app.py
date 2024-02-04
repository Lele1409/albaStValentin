import os

from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import ProfileCreationForm

app = Flask('Alba St Valentin')
app.secret_key = 'verysecretkey badummtss keine Ahnung'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///stv_db.db'
alba_stv_db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
	form = ProfileCreationForm()
	if form.validate_on_submit():
		new_user = User(
			prenom=form.nom.data,
			nom=form.nom.data,
			classe=form.classe.data,
			self_1=form.self_1.data,
			self_2=form.self_2.data,
			self_3=form.self_3.data,
			self_4=form.self_4.data,
			self_5=form.self_5.data,
			self_6=form.self_6.data,
			other_1=form.other_1.data,
			other_2=form.other_2.data,
			other_3=form.other_3.data,
			other_4=form.other_4.data,
			other_5=form.other_5.data,
			other_6=form.other_6.data
		)
		alba_stv_db.session.add(new_user)
		alba_stv_db.session.commit()
		return redirect(url_for('success'))
	return render_template('profilecreator.html', form=form)


@app.route('/success')
def success():
	return render_template('success.html')


if __name__ == '__main__':
	from models import User  # NOQA
	if not os.path.exists(os.path.abspath(r"./instance/stv_db.db")):
		# Create the file with the given context
		with app.app_context():
			alba_stv_db.create_all()

	app.run(debug=True)

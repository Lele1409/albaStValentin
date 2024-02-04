from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import InputRequired, NoneOf, ValidationError


INCOMPLETE_ERROR_MSG = "Veuillez remplir toutes les cases"


class ProfileCreationForm(FlaskForm):
	prenom = StringField('Ton prénom',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG)
						 ])
	nom = StringField('Ton nom',
					  validators=[
						  InputRequired(INCOMPLETE_ERROR_MSG)
					  ])
	classe = SelectField('Ta classe',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', '6ème', '5ème', '4ème', '3ème', '2de', '1ère', 'term', 'prof'])  # NOQA

	self_1 = SelectField('Ton loisir préféré',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', "L'art", 'Le sport', 'La musique', 'Les jeux vidéos'])  # NOQA

	self_2 = SelectField('Genre de film/série préféré',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'Action', 'Drama', 'Thriller', 'Comédie'])  # NOQA

	self_3 = SelectField('Genre de musique préféré',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'Pop', 'Rap', 'Rock', 'Electro'])  # NOQA

	self_4 = SelectField('Plat préféré',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'La pizza', 'Le poulet-frites', 'Les crèspes', 'La mousse au chocolat'])  # NOQA

	self_5 = SelectField('Trait de personnalité',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'Extraverti(e)', 'Introverti(e)'])  # NOQA

	self_6 = SelectField('Trait de personnalité',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'Franche', 'Empathique', 'Confiant', 'Patient'])  # NOQA

	other_1 = SelectField('Loisir préféré',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', "L'art", 'Le sport', 'La musique', 'Les jeux vidéos'])  # NOQA

	other_2 = SelectField('Genre de film/série préféré',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'Action', 'Drama', 'Thriller', 'Comédie'])  # NOQA

	other_3 = SelectField('Genre de musique préféré',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'Pop', 'Rap', 'Rock', 'Electro'])  # NOQA

	other_4 = SelectField('Plat préféré',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'La pizza', 'Le poulet-frites', 'Les crèspes', 'La mousse au chocolat'])  # NOQA

	other_5 = SelectField('Trait de personnalité',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'Extraverti(e)', 'Introverti(e)'])  # NOQA

	other_6 = SelectField('Trait de personnalité',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG),
							 NoneOf(('...', ), message=INCOMPLETE_ERROR_MSG)
							 ],
						 choices=['...', 'Franche', 'Empathique', 'Confiant', 'Patient'])  # NOQA

	submit = SubmitField('Envoye ton profil',
						 validators=[
							 InputRequired(INCOMPLETE_ERROR_MSG)
						 ])

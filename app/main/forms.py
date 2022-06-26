from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    post = TextAreaField('Anything on your mind?', validators=[DataRequired()])
    submit = SubmitField('Submit')

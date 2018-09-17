from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class MinutePitchForm(FlaskForm):
    title = StringField('Blog title',validators=[Required()])
    content = StringField('content',validators=[Required()])
    category = SelectField('Category', choices=[('Choose Category', 'Choose Category'),('emotional', 'emotional'),('skills', 'skills')])
    review = TextAreaField('pitch review', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    
    title = StringField('Comment title',validators=[Required()])
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')    

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please, tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')
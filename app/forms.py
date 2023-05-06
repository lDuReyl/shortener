from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, URL
from .models import URLmodel
from .models import SHORT_LEN
import random
import string

def get_short():
    while True:
        short = ''.join(random.choices(string.ascii_letters + string.ascii_letters, k=SHORT_LEN))
        if URLmodel.query.filter(URLmodel.short == short).first():
            continue
        return short
    

class URLForm(FlaskForm):
    original_url = StringField('Вставьте ссылку',
                           validators=[DataRequired(message='Ссылка не может быть пустой'),
                                       URL(message='Неверная ссылка')])
    submit = SubmitField('Получить короткую ссылку')
    
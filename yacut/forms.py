from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, URL, Length, Optional, Regexp


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите ссылку',
        validators=[DataRequired(
            message='Обязательное поле'),
            URL(message='Проверьте ссылку')
        ]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16), Optional(),
            Regexp(
                r'^[a-zA-Z0-9]+$'
            )
        ]
    )
    submit = SubmitField('Создать')

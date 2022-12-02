from flask import flash, redirect, render_template, request
from urllib.parse import urljoin

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    request_url = request.url
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    short = form.custom_id.data
    if short:
        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!', 'error-message')
            return render_template('index.html', form=form)
    else:
        short = get_unique_short_id()
        while URLMap.query.filter_by(short=short).first():
            short = get_unique_short_id()
    url_map = URLMap(
        original=form.original_link.data,
        short=short
    )
    db.session.add(url_map)
    db.session.commit()
    url_short = urljoin(request_url, short)
    flash(f'{url_short}', 'short_link-message')
    return render_template('index.html', form=form)


@app.route('/<string:url_short>')
def redirect_view(url_short):
    original = URLMap.query.filter_by(short=url_short).first_or_404().original
    return redirect(original)

import random
import string
from app.model import model
from app import db
from flask import Blueprint, render_template, redirect, url_for, request


main_bp=Blueprint("main", __name__)

shortened_url={}

def generate_short_url(length=6):
    chars= string.ascii_letters + string.digits
    while True:
        short_url= "".join(random.choice(chars) for _ in range(length))
        if not model.Url.query.filter_by(short_url=short_url).first():
            return short_url


@main_bp.route("/", methods=['POST','GET'])
def make_short_url():
    new_url=None
    if request.method == 'POST':
        long_url=request.form.get('longUrl')
        short_url=generate_short_url()
        url=model.Url(long_url=long_url, short_url=short_url)
        db.session.add(url)
        db.session.commit()
        new_url = f"{request.url_root}{short_url}"
    return render_template("index.html", new_url=new_url)

@main_bp.route('/<short_url>')
def redirect_to_url(short_url):
    url=model.Url.query.filter_by(short_url=short_url).first()
    if url:
        return redirect(url.long_url)
    return ""
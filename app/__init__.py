from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

db=SQLAlchemy()
migrate=Migrate()
crsf=CSRFProtect()

def create_app():
    app=Flask(__name__)
    
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app,db)
    crsf.init_app(app)
    
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    
    @app.errorhandler(404)
    def not_found(e):
        return "404 NOT FOUND!"    
    return app
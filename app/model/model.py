from app import db

class Url(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    long_url=db.Column(db.Text, nullable=False)
    short_url=db.Column(db.String(225), unique=True,  nullable=False)
    
    def __repr__(self) :
        return f"<Url {self.short_url} → {self.long_url}>"
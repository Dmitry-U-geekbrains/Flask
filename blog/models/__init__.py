from blog.models.user import User
from blog.models.author import Author
from blog.models.article import Article


__all__ = [
    "User",
    "Author",
    "Article",
]



@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")

    
@app.cli.command("create-users")
def create_users():
    from blog.models import User
    admin = User(username="admin", is_staff=True)
    james = User(username="james")
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    
    print("done! created users:", admin, james)
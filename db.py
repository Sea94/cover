import click
from flask_migrate import init, migrate, upgrade

from app import app
from app.models import User, db


@click.group()
def main():
    pass


@main.command()
def removehistories(room):
    with app.app_context():
        History.query.delete()
        db.session.commit()

@main.command()
def removeusers():
    with app.app_context():
        User.query.delete()
        db.session.commit()


@main.command()
def removerequests():
    with app.app_context():
        Request.query.delete()
        db.session.commit()


@main.command()
def seed():
    # os.remove('.db')
    # shutil.rmtree('migrations')
    with app.app_context():
        init()
        migrate()
        upgrade()


if __name__ == "__main__":
    main()

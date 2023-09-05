from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# app作成関数
def create_app():
    app = Flask(__name__)
    # config
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsy",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # 連携
    db.init_app(app)
    Migrate(app, db)

    # crudアプリの登録
    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app

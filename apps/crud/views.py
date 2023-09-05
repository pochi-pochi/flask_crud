from flask import Blueprint, render_template, redirect, url_for
from apps.crud.forms import UserForm
from apps.app import db
from apps.crud.models import User

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
)


# indexエンドポイント
@crud.route("/")
def index():
    return render_template("crud/index.html")


# 新規登録
@crud.route("/users/new", methods=["POST", "GET"])
def create_user():
    form = UserForm()

    if form.submit.data:
        user = User(
            username=form.username.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)


# ユーザー一覧
@crud.route("/users")
def users():
    users = User.query.all()
    return render_template("crud/index.html", users=users)


# 編集
@crud.route("/users/<user_id>", methods=["POST", "GET"])
def edit_user(user_id):
    form = UserForm()

    user = User.query.filter_by(id=user_id).first()

    if form.submit.data:
        user.username = form.username.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))

    return render_template("crud/edit.html", user=user, form=form)


# 削除用
@crud.route("/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))

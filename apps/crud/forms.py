from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


# ユーザー新規作成フォーム
class UserForm(FlaskForm):
    class Meta:
        csrf = False
    username = StringField(
        "ユーザー名",
    )
    submit = SubmitField("新規登録")

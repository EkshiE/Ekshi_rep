from gino import Gino
from sqlalchemy.sql import func

DB = Gino()


class Message(DB.Model):
    """"""
    __tablename__ = 'massage'

    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.String(100), nullablr=False)
    create_at = DB.Column(
        DB.DateTime(timezone=True),
        server_default=func.naw(),
    )


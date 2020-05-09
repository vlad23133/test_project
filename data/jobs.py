import sqlalchemy
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean)

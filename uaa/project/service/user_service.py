from .service import Service
from ..domain.user import User
from .. import db
from sqlalchemy import exc
import logging


class UserService(Service):
    __model__ = User

    def __init__(self, *args, **kwargs):
        super(UserService, self).__init__(*args, **kwargs)

    """ add_user ~ insert User records in db
        :param
            username - <string>
            email - <string>
        :return
            user - <Model.User>
    """

    def add_user(self, username, email):
        try:
            new_user = User(username, email)
            db.session.add(new_user)
            db.session.commit()
            logging.info('Added User<%s, %s', username, email)
            return new_user
        except exc.IntegrityError as error:
            logging.warning('Error trying to add User<%s, %s>', username, email)
            field = 'Username' if 'users_username_key' in error.args[0] else 'Email'
            db.session.rollback()
            raise Exception(field + ' Already Exists.')

    def get_all_users(self):
        try:
            logging.info('Get all users query executed')
            query_all = User.query.all()
            logging.info('%i Users retrieved from db', len(query_all))
            return query_all
        except:  # todo - is possible to get an exception here?
            logging.warning('Error trying to get all Users')
            raise

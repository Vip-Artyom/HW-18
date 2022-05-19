from dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Genre).get(mid)

    def get_all(self):
        return self.session.query(Genre).all()

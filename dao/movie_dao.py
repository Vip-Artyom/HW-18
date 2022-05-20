from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()
        self.session.close()

        return movie

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()
        self.session.close()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
        self.session.close()

    def movies_by_filter_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did)

    def movies_by_filter_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid)

    def movies_by_filter_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

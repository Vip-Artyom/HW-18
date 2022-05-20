from dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.id = data["id"]
        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        if "id" in data:
            movie.id = data["id"]
        if "title" in data:
            movie.title = data["title"]
        if "description" in data:
            movie.description = data["description"]
        if "trailer" in data:
            movie.trailer = data["trailer"]
        if "year" in data:
            movie.year = data["year"]
        if "rating" in data:
            movie.rating = data["rating"]
        if "genre_id" in data:
            movie.genre_id = data["genre_id"]
        if "director_id" in data:
            movie.director_id = data["director_id"]

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)

    def movies_by_director(self, did):
        return self.dao.movies_by_filter_director(did)

    def movies_by_genre(self, genre):
        return self.dao.movies_by_filter_genre(genre)

    def movies_by_year(self, year):
        return self.dao.movies_by_filter_year(year)

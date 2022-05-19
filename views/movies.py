from flask import request
from flask_restx import Resource, Namespace
from container import movie_service
from dao.models.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")

        all_movies = movie_service.get_all()

        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.get_json()

        movie_service.create(req_json)

        return "", 201


@movie_ns.route('/<int:mid>')
class MoviesView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)

        if not movie:
            return f"Нет фильма с  id {mid}", 404

        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.get_json()
        req_json["id"] = mid

        movie_service.update(req_json)

        return "Обновлен", 204

    def patch(self, mid):
        req_json = request.get_json()
        req_json["id"] = mid

        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)

        return "", 204

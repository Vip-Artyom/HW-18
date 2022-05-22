from flask import request, jsonify
from flask_restx import Resource, Namespace
from container import movie_service
from dao.models.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        try:
            director_id = request.args.get("director_id")
            genre_id = request.args.get("genre_id")
            year = request.args.get("year")

            if director_id is not None:
                all_movies = movie_service.movies_by_director(director_id)
            elif genre_id is not None:
                all_movies = movie_service.movies_by_genre(genre_id)
            elif year is not None:
                all_movies = movie_service.movies_by_year(year)
            else:
                all_movies = movie_service.get_all()

            return movies_schema.dump(all_movies), 200

        except Exception as e:
            print(e)

    def post(self):
        req_json = request.get_json()
        movie_id = req_json["id"]
        movie_service.create(req_json)

        responce = jsonify()
        responce.status_code = 201
        responce.headers["Location"] = f"{movie_id}"
        return responce


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

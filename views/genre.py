from flask_restx import Namespace, Resource
from container import genre_service
from dao.models.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()

        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)

        if not genre:
            return f"Нет жанра с id {gid}", 404

        return genre_schema.dump(genre), 200

from flask_restx import Namespace, Resource
from container import director_service
from dao.models.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:did>')
class DirectorsView(Resource):
    def get(self, did):
        director = director_service.get_one(did)

        if not director:
            return f"Нет режиссера с id {did}", 404

        return director_schema.dump(director), 200

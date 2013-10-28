import datetime
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongorest import MongoRest
from flask.ext.mongorest.views import ResourceView
from flask.ext.mongorest.resources import Resource
from flask.ext.mongorest import operators as ops
from flask.ext.mongorest import methods  


app = Flask(__name__)

app.config.update(
    MONGODB_HOST = 'localhost',
    MONGODB_PORT = '27017',
    MONGODB_DB = 'mongorest_example_app',
)

db = MongoEngine(app)
api = MongoRest(app)

class Location(db.EmbeddedDocument):
    # This is only gonna work if it's in SF so not required.
    name = db.StringField(required=True)
    longitude = db.FloatField(required=True)
    latitude = db.FloatField(required=True)

    def __unicode__(self):
        return self.name

class LocationResource(Resource):
	document = Location

class Confession(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    primary_sin = db.StringField(required=True)
    secondary_sin = db.StringField(required=True)
    gender = db.StringField(max_length=255, required=False)
    location = db.EmbeddedDocumentField(Location, required=True)

    def get_absolute_url(self):
        return url_for('confession', kwargs={"id": self.id})

    def __unicode__(self):
        return self.created_at.strftime('%H:%M %Y-%m-%d')


class ConfessionResource(Resource):
    document = Confession
    related_resources = {
        'location': LocationResource,
    }

@api.register(name='list', url='/confessions/')
class ConfessionsView(ResourceView):
    resource = ConfessionResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List]

if __name__ == "__main__":
    app.run()
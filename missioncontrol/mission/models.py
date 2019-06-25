from mongoengine import StringField, connect, Document, ReferenceField, FloatField, IntField

connect("mission")


class Mission(Document):
    name = StringField(required=True, max_length=200)
    drone = StringField(required=True, max_length=100)


class MissionStep(Document):
    mission = ReferenceField(Mission)
    order = IntField(required=True)
    command = StringField(required=True, max_length=50)
    sleep = FloatField(required=False)

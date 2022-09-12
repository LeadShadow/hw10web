from datetime import datetime

from mongoengine import *

connect(host='mongodb://localhost:27017/test')


class Addressbook(Document):
    name = StringField(max_length=100, min_length=1, required=True)
    phone = StringField(max_length=100, default='')
    birthday = DateTimeField(max_length=100, default='', null=True)
    emails = StringField(max_length=100, default='')
    address = StringField(max_length=120, default='')


class Tags(Document):
    id_count = IntField()
    tags = ListField(StringField(max_length=80))


class Note(Document):
    id_count = IntField()
    text = StringField(max_length=1000)
    done = BooleanField(default=False)
    created = DateTimeField(default=datetime.now())
    tags = ReferenceField(Tags, reverse_delete_rule=CASCADE, dbref=True)


class Archived(Document):
    id_count = IntField()
    text = StringField(max_length=1000)
    transferred = DateTimeField(default=datetime.now())
    tags = ReferenceField(Tags, reverse_delete_rule=CASCADE, dbref=True)


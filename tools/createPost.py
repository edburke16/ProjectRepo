#! tools-env/bin/python

from mongoengine import connect, Document, EmailField, StringField, BooleanField, DateTimeField, ReferenceField, IntField

connect(db='project',
    host = 'localhost',
    port = 27017)

class User(Document):
    email = EmailField(required = True, unique = True)
    alias = StringField(required = True, unique = True)
    password = StringField(min_length = 8, required = True)
    emailVerified = BooleanField(default = False)
    lastLogin = DateTimeField()
    allowTracking = BooleanField(default = False)
    isMod = BooleanField(default = False)

class Posts(Document):
    #max length of title is 140 characters
    title = StringField(required = True, max_length = 140)
    author = ReferenceField(User)
    #max length of content is 10000 characters
    content = StringField(max_length = 10000)
    score = IntField(default = 0)

alias = raw_input('alias: ')

title = raw_input('title: ')

content = raw_input('post (Not required.  Must be under 1000 characters): ')

try:
    user = User.objects(alias=alias)[0]  # returns user object by alias
    post = Posts(author=user, title=title, content=content)

    post.save()

except IndexError:
    print('Failed to find user %s', alias)

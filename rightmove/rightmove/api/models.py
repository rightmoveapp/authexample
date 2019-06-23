from django.db.models import Model, CharField



class Content(Model):
    instance_name = CharField(max_length=100)
    content_body = CharField(max_length=5000)
    css_tag = CharField(max_length=200)

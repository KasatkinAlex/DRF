from rest_framework import serializers


class OtherResourcesValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        try:
            tmp_val = val.lower()
        except AttributeError:
            tmp_val = ''
        if tmp_val.lower().count('https//') and not tmp_val.lower().count('https//youtube.com'):
            raise serializers.ValidationError("есть ссылка на сторониий сайт")



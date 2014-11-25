from django.db import models


class MyManager(models.Manager):
    def update_or_create(self, filter_attrs, attrs):
        try:
            obj = self.get(**filter_attrs)
            changed = False
            for k, v in attrs.items():
                if obj.__dict__[k] != v:
                    changed = True
                    obj.__dict__[k] = v
            if changed:
                obj.save()
                return 'updated'
            return 'unchanged'
        except self.model.DoesNotExist:
            attrs.update(filter_attrs)
            self.create(**attrs)
            return 'created'


class Album(models.Model):
    title = models.CharField(max_length=200)

    objects = MyManager()


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks')
    title = models.CharField(max_length=200)

    objects = MyManager()

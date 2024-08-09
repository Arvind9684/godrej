import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.apps import apps

@receiver(post_delete)
def delete_related_files(sender, instance, **kwargs):
    # Loop through all file fields in the model
    for field in instance._meta.fields:
        if field.get_internal_type() == 'FileField':
            file = getattr(instance, field.name)
            if file and os.path.isfile(file.path):
                os.remove(file.path)

# Dynamically connect the signal to all models
def connect_signals():
    for model in apps.get_models():
        post_delete.connect(delete_related_files, sender=model)

@receiver(post_delete)
def delete_related_files(sender, instance, **kwargs):
    def delete_files(model_instance):
        for field in model_instance._meta.fields:
            if field.get_internal_type() == 'FileField':
                file = getattr(model_instance, field.name)
                if file and os.path.isfile(file.path):
                    os.remove(file.path)

    # Delete files from the instance being deleted
    delete_files(instance)
    
    # Delete files from related instances
    for related_object in instance._meta.related_objects:
        related_name = related_object.get_accessor_name()
        related_manager = getattr(instance, related_name)
        if related_object.one_to_one:
            related_instance = related_manager
            delete_files(related_instance)
        else:
            for related_instance in related_manager.all():
                delete_files(related_instance)


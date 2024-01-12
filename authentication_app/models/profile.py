import os
import shutil

from django.db.models.signals import pre_save
from django.dispatch import receiver

from WorkPal import settings
from pathlib import Path
from django.db import models
from authentication_app.models import CustomUser


class Profile(models.Model):
    @staticmethod
    def get_file_extension(file_path):
        """
        Get the extension of a file and return it

        :param file_path: ASDF54321.jpg
        :return: .jpg
        """

        return Path(file_path).suffix

    @staticmethod
    def get_absolute_path_to_user_profile_storage(user_id):
        return settings.MEDIA_ROOT + f'/images/profiles/user_{user_id}'

    @staticmethod
    def get_relative_path_to_user_profile_storage(user_id):
        return f'images/profiles/user_{user_id}'

    def user_directory_path(instance, filename):
        """
        File will be uploaded to the returned end path;
        in this case, the file will be uploaded to
            MEDIA_ROOT/images/profiles/user_<id>/profile_picture<extension>

        :param filename: ASDF54321.jpg
        :return: images/profiles/user_<id>/profile_picture.jpg
        """

        extension = Profile.get_file_extension(filename)
        result = f'{Profile.get_relative_path_to_user_profile_storage(instance.user_id)}' \
                 f'/profile_picture{extension}'
        return result

    def delete(self, *args, **kwargs):
        """
        Extend the delete functionality to delete the user's media folder along with its entity in the db
        """

        user_id = self.user_id

        try:
            shutil.rmtree(Profile.get_absolute_path_to_user_profile_storage(user_id))
        except OSError as e:
            raise Exception(f'Could not delete the media folder of the user: {e.filename} - {e.strerror}.')

        super().delete(*args, **kwargs)

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to=user_directory_path, default='images/default/default_img.jpg')


@receiver(pre_save, sender=Profile)
def delete_old_profile_pic_when_save(sender, *args, **kwargs):
    """
    Deletes the existing profile picture to avoid name conflicts with new uploads.
    """

    instance = kwargs['instance']
    path = Profile.get_absolute_path_to_user_profile_storage(instance.user_id)

    if os.path.exists(path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print(files)

        for f in files:
            if 'profile_picture' in f:
                os.remove(path + '/' + f)
                break

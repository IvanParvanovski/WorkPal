from accounts_app.models import CustomUser
from accounts_app.models.profile import Profile
from services.interfaces.accounts_app.profile_interface import ProfileInterface


class ProfileService(ProfileInterface):
    @staticmethod
    def create_profile(user: CustomUser,
                       job_title: str,
                       description: str,
                       image_path: str):

        profile = Profile.objects.create(
            user=user,
            job_title=job_title,
            description=description,
            image=image_path
        )

        return profile

    @staticmethod
    def get_all_profiles():
        return Profile.objects.all()

    @staticmethod
    def get_profile_by_id(_id: int) -> Profile:
        return Profile.objects.get(id=_id)

    @staticmethod
    def delete_profile(profile: Profile):
        profile.delete()

    @staticmethod
    def delete_profile_by_id(_id: int):
        profile = ProfileService.get_profile_by_id(_id)

        ProfileService.delete_profile(profile)

    @staticmethod
    def edit_profile_by_id(_id: int,
                           job_title: str,
                           description: str,
                           image_path: str):

        profile = ProfileService.get_profile_by_id(_id=_id)

        profile.job_title = job_title
        profile.description = description
        profile.image_path = image_path

        profile.save()
        return profile

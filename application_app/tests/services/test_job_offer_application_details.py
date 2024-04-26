from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from services.generic.application_app.job_offer_application_details_service import JobOfferApplicationDetailsService


class JobOfferApplicationDetailsTestCase(TestCase):
    def setUp(self):
        self.random_motivation_letter = 'random motivation letter'
        self.random_cv = '/default/images/cv.png'

    def test_create_job_offer_application_details_should_add_new_job_offer_application_details_when_commit_is_not_given(self):
        job_offer_application_details = JobOfferApplicationDetailsService.create_job_offer_details(
            motivation_letter=self.random_motivation_letter,
            cv=self.random_cv
        )

        try:
            created_details = JobOfferApplicationDetailsService.get_job_offer_details_by_id(job_offer_application_details.id)
        except ObjectDoesNotExist:
            created_details = None

        self.assertIsNotNone(created_details)
        self.assertEqual(created_details, job_offer_application_details)
        self.assertEqual(self.random_motivation_letter, created_details.motivation_letter)
        self.assertEqual(self.random_motivation_letter, job_offer_application_details.motivation_letter)
        self.assertEqual(self.random_cv, job_offer_application_details.cv)

    def test_create_job_offer_application_details_should_add_new_job_offer_application_details_when_commit_is_true(self):
        job_offer_application_details = JobOfferApplicationDetailsService.create_job_offer_details(
            motivation_letter=self.random_motivation_letter,
            cv=self.random_cv,
            commit=False
        )

        try:
            created_details = JobOfferApplicationDetailsService.get_job_offer_details_by_id(
                job_offer_application_details.id)
        except ObjectDoesNotExist:
            created_details = None

        self.assertIsNone(created_details)

    def test_create_job_offer_application_details_should_not_add_job_offer_application_details_when_commit_is_false(self):

        job_offer_application_details = JobOfferApplicationDetailsService.create_job_offer_details(
            motivation_letter=self.random_motivation_letter,
            cv=self.random_cv,
            commit=False
        )

        try:
            created_details = JobOfferApplicationDetailsService.get_job_offer_details_by_id(
                job_offer_application_details.id)
        except ObjectDoesNotExist:
            created_details = None

        self.assertIsNone(created_details)

    def test_get_all_job_offer_application_details_should_return_all_job_offers_application_details(self):

        for i in range(0, 5):
            job_offer_application_details = (JobOfferApplicationDetailsService
                                               .create_job_offer_details(
                                                    motivation_letter=f'{self.random_motivation_letter}_{i}',
                                                    cv=self.random_cv))

        job_offer_application_details_count = JobOfferApplicationDetailsService.get_all_job_offer_details().count()

        self.assertEqual(5, job_offer_application_details_count)

    def test_get_job_offer_application_details_by_id_should_return_details_when_id_is_passed(self):
        motivation_letter = 'random motivation letter'

        job_offer_application_details = JobOfferApplicationDetailsService.create_job_offer_details(
            motivation_letter=motivation_letter, cv=self.random_cv
        )
        returned_object = JobOfferApplicationDetailsService.get_job_offer_details_by_id(_id=job_offer_application_details.id)

        self.assertEqual(job_offer_application_details, returned_object)

    def test_get_job_offer_application_details_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            JobOfferApplicationDetailsService.get_job_offer_details_by_id(_id=-1)

        self.assertEqual('JobOfferApplicationDetails matching query does not exist.', str(context.exception))

    def test_delete_job_offer_application_details_should_delete_details_when_application_is_provided(self):

        job_offer_application_details = JobOfferApplicationDetailsService.create_job_offer_details(
            self.random_motivation_letter,
            self.random_cv
        )

        try:
            created_entity = JobOfferApplicationDetailsService.get_job_offer_details_by_id(job_offer_application_details.id)
        except ObjectDoesNotExist:
            created_entity = None

        self.assertIsNotNone(created_entity)

        JobOfferApplicationDetailsService.delete_job_offer_details(job_offer_application_details)

        try:
            created_entity = JobOfferApplicationDetailsService.get_job_offer_details_by_id(job_offer_application_details.id)
        except ObjectDoesNotExist:
            created_entity = None

        self.assertIsNone(created_entity)

    def test_delete_job_offer_application_details_should_raise_exception_when_the_details_does_not_exist(self):
        motivation_letter = 'random motivation letter'

        job_offer_application_details = JobOfferApplicationDetailsService.create_job_offer_details(
            motivation_letter=motivation_letter,
            cv=self.random_cv
        )
        JobOfferApplicationDetailsService.delete_job_offer_details(job_offer_application_details)

        with self.assertRaises(ValueError) as context:
            JobOfferApplicationDetailsService.delete_job_offer_details(job_offer_application_details)

        self.assertIn('JobOfferApplicationDetails object can\'t be deleted because its id attribute is set to None.', str(context.exception))

    def test_delete_job_offer_application_details_by_id_should_delete_details_when_valid_id_is_provided(self):
        job_offer_application_details = JobOfferApplicationDetailsService.create_job_offer_details(
            motivation_letter=self.random_motivation_letter,
            cv=self.random_cv
        )

        try:
            created_entity = JobOfferApplicationDetailsService.get_job_offer_details_by_id(job_offer_application_details.id)
        except ObjectDoesNotExist:
            created_entity = None

        self.assertIsNotNone(created_entity)

    def test_delete_job_offer_application_details_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            JobOfferApplicationDetailsService.get_job_offer_details_by_id(_id=-1)

        self.assertEqual('JobOfferApplicationDetails matching query does not exist.', str(context.exception))

    def test_update_job_offer_application_details_by_id_should_update_details_when_commit_is_not_given(self):
        motivation_letter = 'random motivation letter'
        new_motivation_letter = 'new motivation letter'

        job_offer_application_details = JobOfferApplicationDetailsService.create_job_offer_details(
            motivation_letter=motivation_letter,
            cv=self.random_cv
        )

        JobOfferApplicationDetailsService.edit_job_offer_by_id(_id=job_offer_application_details.id,
                                                               motivation_letter=new_motivation_letter)

        changed_project_application_details = (JobOfferApplicationDetailsService
                                               .get_job_offer_details_by_id(job_offer_application_details.id))

        self.assertEqual(new_motivation_letter, changed_project_application_details.motivation_letter)


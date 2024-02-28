from listing_app.models.listing import Listing
from services.interfaces.listing_app.listing_interface import ListingInterface


class ListingService(ListingInterface):
    @staticmethod
    def create_listing(title: str,
                       location: str,
                       images: str,
                       description: str) -> Listing:

        listing = Listing.objects.create(
            title=title,
            location=location,
            images=images,
            description=description,
        )

        listing.save()
        return listing

    @staticmethod
    def get_all_listings():
        return Listing.objects.all()

    @staticmethod
    def get_listing_by_id(_id: int):
        return Listing.objects.get(id=_id)

    @staticmethod
    def delete_listing(listing):
        listing.delete()

    @staticmethod
    def delete_listing_by_id(_id: int):
        listing = ListingService.get_listing_by_id(_id)
        listing.delete()

    @staticmethod
    def edit_listing_by_id(_id: int,
                           title: str,
                           location: str,
                           images: str,
                           description: str) -> Listing:

        listing = ListingService.get_listing_by_id(_id)

        listing.title = title
        listing.location = location
        listing.images = images
        listing.description = description

        listing.save()
        return listing

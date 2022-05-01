import datetime


class Person:
    def __init__(self, id, first_name, last_name, city, address, phone_number=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.city = city
        self.address = address


class Parking:
    def __init__(self, parking_type, parking_places):
        self.parking_type = parking_type
        self.parking_places = parking_places


class RealEstate:

    def __init__(self, owner:Person, city, address, rooms_num, sq_m, balconies_num, parking=None):
        self.id = datetime.datetime.utcnow().timestamp()
        self.owner = owner
        self.city = city
        self.address = address
        self.rooms_num = rooms_num
        self.sq_m = sq_m
        self.balconies_num = balconies_num
        self.parking = parking


class Flat(RealEstate):

    def __init__(self, city, address, rooms_num, sq_m, balconies_num, floor, has_elevator):
        super().__init__(city, address, rooms_num, sq_m, balconies_num)
        self.floor = floor
        self.has_elevator = has_elevator


class Villa(RealEstate):

    def __init__(self, city, address, rooms_num, sq_m, balconies_num, floors_num, outer_area, has_pool):
        super().__init__(city, address, rooms_num, sq_m, balconies_num)
        self.floors_num = floors_num
        self.outer_area = outer_area
        self.has_pool = has_pool


class Listing:
    def __init__(self, real_estate_id: int):
        self.id = datetime.datetime.utcnow().timestamp()
        self.real_estate_id = real_estate_id
        self.publish_date = datetime.date.today()
        self.state = "open"  # "closed", "cancelled", "suspended"


class RentListing(Listing):
    def __init__(self, real_estate_id: int,
                 price_per_month: int, months_ahead: int, pets_allowed: bool, smoking_allowed: bool):
        super().__init__(real_estate_id)
        self.price_per_month = price_per_month
        self.months_ahead = months_ahead
        self.smoking_allowed = smoking_allowed
        self.pets_allowed = pets_allowed


class SaleListing(Listing):
    def __init__(self, real_estate_id: int,
                 price: int, registered_in_tabu: bool):
        super().__init__(real_estate_id)
        self.price = price
        self.registered_in_tabu = registered_in_tabu


class Deal:
    def __init__(self, listing_id, comission):
        self.listing_id = listing_id
        self.comission = comission


class RealEstateAgency:

    def __init__(self):
        self.real_estates = {}  # maps from real_estate_id to real estate
        self.listings = {}  # maps real_estate_id to list of listings
        self.closed_deals = []

    def add_real_estate(self):
        pass

    def add_rent_listing(self, real_estate_id: int, price_per_month: int,
                         months_ahead: int, pets_allowed: bool, smoking_allowed: bool):

        if real_estate_id not in self.real_estates:
            print(f"Real estate does not exist in the system, create real estate first!")
            return False

        # todo - what should happen in listing for rent for this real estate already exists?

        for listing in self.listings.get(real_estate_id):
            if listing.state == 'open' and isinstance(listing, RentListing):
                print("Rent listing for this real estate already exists")
                return False

        if real_estate_id not in self.listings:
            self.listings[real_estate_id] = \
                RentListing(real_estate_id, price_per_month, months_ahead, pets_allowed, smoking_allowed)

    def delete_listing(self):
        pass

    def get_all_real_estates(self):
        return self.real_estates

    def close_deal(self, listing_id):
        pass


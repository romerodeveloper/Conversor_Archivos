from pickletools import read_uint1


class Catalogo:

    def __init__(self, id=None, common=None, botanical=None, zone=None, ligth=None, price=None, availability=None):
        self._id = id
        self._common = common
        self._botanical = botanical
        self._zone = zone
        self._ligth = ligth
        self._price = price
        self._availability = availability
    
    def __str__(self) -> str:
        return f'''
        ID: {self._id}
        COMMON: {self._common}, BOTANICAL: {self._botanical},
        ZONE: {self._zone}, LIGTH: {self._ligth}
        PRICE: {self._price}, AVAILABILITY: {self._availability}
        '''
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def common(self):
        return self._common

    @common.setter
    def common(self, common):
        self._common = common

    @property
    def botanical(self):
        return self._botanical

    @botanical.setter
    def botanical(self, botanical):
        self._botanical = botanical

    @property
    def zone(self):
        return self._zone

    @zone.setter
    def zone(self, zone):
        self._zone = zone

    @property
    def ligth(self):
        return self._ligth

    @ligth.setter
    def ligth(self, ligth):
        self._ligth = ligth

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
        
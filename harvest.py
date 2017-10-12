############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('muskmelon', 'musk', '1998', 'green', True, True)
    muskmelon.add_pairing('mint')
    casaba = MelonType('casaba', 'cas', '2003', 'orange', False, None)
    casaba.add_pairing('mint')
    casaba.add_pairing('stawberries')
    crenshaw = MelonType('crenshaw', 'cren', '1996', 'green', False, None)
    crenshaw.add_pairing('prosciutto')
    yellow_watermelon = MelonType('yellow_watermelon', 'yw', '2013', 'yellow', False, True)
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])
    return all_melon_types


def print_melon_pairings(all_melon_types):
    """Takes a list of melons and prints pairings."""

    for melon in all_melon_types:
        print "{name} pairs with".format(name=melon.name)

        for pairing in melon.pairings:
            print "- ", pairing


melon_list = make_melon_types()
print_melon_pairings(melon_list)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_dict = {}
    for melon in melon_types:
        melon_type_dict[melon.code] = melon

    return melon_type_dict


melon_dict = make_melon_type_lookup(melon_list)
print melon_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, num, melon_type, shape, color, field, harvester):
        """Creates a record of harvested melon."""

        self.num = int(num)
        self.melon_type = melon_type
        self.shape = int(shape)
        self.color = int(color)
        self.field = int(field)
        self.harvester = harvester

    def is_sellable(self):
        """ """

        if self.shape > 5 and self.color > 5 and self.field != 3:
            return "CAN BE SOLD"
        else:
            return "NOT SELLABLE"


def make_melons():
    """Returns a list of Melon objects."""

    yw = melon_dict['yw']
    cas = melon_dict['cas']
    cren = melon_dict['cren']
    musk = melon_dict['musk']

    Melon_1 = Melon(1, yw, 8, 7, 2, 'Sheila')
    Melon_2 = Melon(2, yw, 3, 4, 2, 'Sheila')
    Melon_3 = Melon(3, yw, 9, 8, 3, 'Sheila')
    Melon_4 = Melon(4, cas, 10, 6, 35, 'Sheila')
    Melon_5 = Melon(5, cren, 8, 9, 35, 'Michael')
    Melon_6 = Melon(6, cren, 8, 2, 35, 'Michael')
    Melon_7 = Melon(7, cren, 2, 3, 4, 'Michael')
    Melon_8 = Melon(8, musk, 6, 7, 4, 'Michael')
    Melon_9 = Melon(9, yw, 7, 10, 3, 'Sheila')

    harvest_melon_list = []
    harvest_melon_list.extend([Melon_1, Melon_2, Melon_3, Melon_4, Melon_5,
                      Melon_6, Melon_7, Melon_8, Melon_9])

    return harvest_melon_list

harvested_melons = make_melons()
# Melon_1, Melon_2, Melon_3, Melon_4, Melon_5, Melon_6, Melon_7, Melon_8, Melon_9 = harvested_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # if with three conditions, return a boolean




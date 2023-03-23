############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def __repr__(self):
        return f"<Melon Name: {self.name} Melon Code: {self.code}>"

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk","Muskmelon",1998,"green",True,True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas","Casaba",2003,"orange",False,False)
    cas.add_pairing("strawberry")
    cas.add_pairing("mint")
    all_melon_types.append(cas)
    
    cren = MelonType("cren","Crenshaw",1996,"green",False,False)
    all_melon_types.append(cren)

    yw = MelonType("yw","Yellow Watermelon",2013,"yellow",False,True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types

print(make_melon_types)
#returns a list of current melon types

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    #melon_types needs to be a dictionary/object with all melon data
    #loop through the dictionary and identify the print(f"{melon.names} + {melon.pairings}"")

    for melons in melon_types:
        print(f"{melons.name} pairs with {melons.pairings}")

#print(print_pairing_info(melon_types))

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    retval = {}

    for names in melon_types:
        if names.code not in retval:
            retval[names.code] = names 
    return retval

#thing = make_melon_type_lookup(melon_types)
#print(thing)


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, type, shape, color, field_number, harvester):

        self.type = type
        self.shape = shape
        self.color = color
        self.field_number = field_number
        self.harvester = harvester

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types): 
    """Returns a list of Melon objects."""

    #musk = MelonType("musk","Muskmelon",1998,"green",True,True)
    #where is our melon data? make melon type look up function... 

    retval = []

    melon_data = make_melon_type_lookup(melon_types) #this gives us a list of dictionary objects

    melon1 = Melon(melon_data["yw"], 8,7,2,"Shiela")
    retval.append(melon1)

    melon2 = Melon(melon_data["yw"],3,4,2,"Shiela")
    retval.append(melon2)

    melon3 = Melon(melon_data["yw"],9,8,3,"Shiela")
    retval.append(melon3)

    melon4 = Melon(melon_data["cas"],10,6,35,"Shiela")
    retval.append(melon4)

    melon5 = Melon(melon_data["cren"],8,9,35,"Michael")
    retval.append(melon5)

    melon6 = Melon(melon_data["cren"],8,2,35,"Michael")
    retval.append(melon6)

    melon7 = Melon(melon_data["cren"],2,3,4,"Michael")
    retval.append(melon7)

    melon8 = Melon(melon_data["musk"],6,7,4,"Michael")
    retval.append(melon8)

    melon9 = Melon(melon_data["yw"],7,10,3,"Shiela")
    retval.append(melon9)

    return retval

melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for elements in melons:
        harvester = f"Harvested by {elements.harvester}"
        field = f"Field #{elements.field}"

        if elements.is_sellable():
            sellable = "CAN BE SOLD"
        else:
            sellable = "NOT SELLABLE"
        
        print(f"{harvester} from {field} {sellable}")

    # Fill in the rest

#you can fix part one by looking on line 58
#validate 105 with 140
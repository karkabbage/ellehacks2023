from dataclasses import dataclass

"""

programmers: Erin Kim, Karyna Lim
date: Feb 18 2023
goal: win elle-hacks win bluetooth headphones -- and nintendo switch --
 lets win both at once

essential functionalities 
1) autcomplete words, ~ woordle similar
2) mapping location
3) 
4)


Dear judge, 

"""

# major word bank of all sub categories of recyclibles
word_bank = {"battery": 7, "light bulb": 3, "mirror": 8, "matress": 2,
             "paint": 3, "pesticide": 4, "computer": 8, "phone": 9, "syringe": 5, "needle": 3,
             "aerosol": 2, "gasoline": 9, "cleaner": 4, "cd": 2, "sunglasses": 4, "glasses": 2}


def autocomplete_search(customer_word: str) -> str:
    """
    suggest words from word bank of all possible non-conventional recyclibles in real time

    Preconditions:
    - you may ASSUME that every letter typed automatically calls this function
    - ASSUME ties between values have no effect, it will return the first occurence of the value
    - customer_word letters are all miniscule and are at most, the starting letters / prefix of the word

    # doctests to portray how app would react
    >>> autocomplete_search("p")
    'phone'
    >>> autocomplete_search("pa")
    'paint'
    >>> autocomplete_search("comp")
    'computer'

    """

    # TODO loop function to go thru entire word bank
    cust_word_length = len(customer_word)

    relevant_word_set = {}
    for word in word_bank:
        if customer_word in word and word[0] == customer_word[0] and cust_word_length <= len(word):
            relevant_word_set[word] = word_bank[word]

    if relevant_word_set == {}:
        # this would send the user to a page with no image results, just the text
        return " sorry, this item is unavailible "

    else:
        # this returned word would be based off of word search relevency values
        return max(relevant_word_set, key=relevant_word_set.get)



@dataclass
class DisposalInfo:
    """ A class to search the closest location of disposals corresponding to the given category and location coordinates.

    Instance Attributes:
        - location, city name
        - coordinates, of the actual disposal factory
        - category, str of specefic disposal items, ex: battery, light bulb,
        - name of disposal factory,

    Preconditions:
        - self.location in battery_locations
        - self.category in word_bank


    >>> erins_lightbulb_garabage_place = DisposalInfo(location="toronto", coordinates=(45, 60), category="batteries", factory_name="erin")

    """

    location: str
    coordinates: tuple
    category: str
    factory_name: str


# example list of all LocationSearch
first_location = DisposalInfo(location="richmond hill", coordinates= (43.77, 79.50), category = "battery", factory_name="sally's battery disposal")
second_location = DisposalInfo(location="richmond hill", coordinates= (43.85, 79.33), category="battery", factory_name="bob's factory")
third_location = DisposalInfo(location="richmond hill", coordinates= (43.65, 79.38), category="light bulb", factory_name="june's fluroscent trap")
fourth_location = DisposalInfo(location="markham", coordinates= (30.53, 41.22), category="battery", factory_name="bye bye battery")
battery_locations = [first_location, second_location, third_location, fourth_location]

def location_search(user_coords:tuple[float, float], location_name:str, user_category:str) -> str:
    """ given the coordinates of our user, return the name and coordinates of the closest disposal factory.
    If no location exists for a user's category from their chosen location, suggest that the user try a different location.

    - you may ASSUME that there is atleast one location with the same category in the battery_locations data set list

    """
    possible_locations = []

    for disposal_locations in battery_locations:
        if disposal_locations.category == user_category and disposal_locations.location == location_name:
            possible_locations.append(disposal_locations)

    if possible_locations == []:
        secondary_location_search()

    else:
        optimal_disposal = (100000000000, 100000000000)

        for disposal_locations in possible_locations:
            x_user_coord = user_coords[0]
            y_user_coord = user_coords[1]

            x_coord = disposal_locations.coordinates[0]
            y_coord = disposal_locations.coordinates[1]

            distance = ( (x_coord - x_user_coord)**2 + (y_coord - y_user_coord)**2 ) ** 0.5
            if distance < optimal_disposal:
                optimal_disposal = disposal_locations


        return "The closest disposal near you is " + disposal_locations.factory_name + ", located at " + disposal_locations.coordinates + "."


def secondary_location_search(user_coords:tuple[float, float], location_name:str, user_category:str) -> str:

    possible_locations = []

    for disposal_locations in battery_locations:
        if disposal_locations.category == user_category and disposal_locations.location != location_name:
            possible_locations.append(disposal_locations)

    for disposal_locations in possible_locations:
                x_user_coord = user_coords[0]
                y_user_coord = user_coords[1]

                x_coord = disposal_locations.coordinates[0]
                y_coord = disposal_locations.coordinates[1]

                distance = ( (x_coord - x_user_coord)**2 + (y_coord - y_user_coord)**2 ) ** 0.5
                if distance < optimal_disposal:
                    optimal_disposal = disposal_locations

    return "The closest disposal near you is not in your given location. The disposal location is " + disposal_locations.factory_name + ", located at " + disposal_locations.coordinates + ". "

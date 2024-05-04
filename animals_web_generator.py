import json

filepath = "animals_data.json"


def load_data(file):
    """
    Loading the initial json file as a whole
    :param file: filepath to the json file
    :return: the json file as a dict in python
    """
    with open(file, "r") as handle:
        return json.load(handle)


def get_animal_information(animals_data, number):
    """
    Gets the required Data for each animal by specified number in the list!
    :param animals_data: array of animals from json file
    :param number: number of the animal in the array of animals
    :return: Either tuple of name, diet, locations, animal_type or name, diet, locations
    depending on if a type exists
    """

    animal = animals_data[number]
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    locations = animal["locations"]     #may result in a list
    locations = ", ".join(locations)    #makes list to a string of locations

    try:
        animal_type = animal["characteristics"]["type"]
        return (name, diet, locations, animal_type)

    except KeyError:
        return (name, diet, locations)


def main():
    """

    :return:
    """
    animals_data = load_data(filepath)
    animal_count = len(animals_data)

    for animal_number in range(0, animal_count):
        animals_processed = get_animal_information(animals_data, animal_number)
        if len(animals_processed) == 4:
            name, diet, locations, animal_type = animals_processed
            print(name)
            print(diet)
            print(locations)
            print(animal_type)
            print("---")
        elif len(animals_processed) == 3:
            name, diet, locations = animals_processed
            print(name)
            print(diet)
            print(locations)
            print("---")


if __name__ == "__main__":
    main()

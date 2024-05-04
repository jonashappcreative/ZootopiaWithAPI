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

    output_html = ""

    for animal_number in range(0, animal_count):
        animals_processed = get_animal_information(animals_data, animal_number)
        if len(animals_processed) == 4:
            name, diet, locations, animal_type = animals_processed
            output_html += f"Name: {name}\n"
            output_html += f"Diet: {diet}\n"
            output_html += f"Locations: {locations}\n"
            output_html += f"Type: {animal_type}\n\n"

        elif len(animals_processed) == 3:
            name, diet, locations = animals_processed
            output_html += f"Name: {name}\n"
            output_html += f"Diet: {diet}\n"
            output_html += f"Locations: {locations}\n\n"

    with open("animals_template.html", "r") as html_file:
        template_content = html_file.read()

    # Replace the placeholder with the generated animal information
    updated_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output_html)

    # Write the updated HTML content into a new HTML file
    with open("animals_filled_with_data.html", "w") as output_file:
        output_file.write(updated_html_content)


if __name__ == "__main__":
    main()

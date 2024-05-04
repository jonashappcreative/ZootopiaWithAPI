import json
import os

import requests

filepath = "animals_data.json"
API_KEY = "wbvM4JFhbZZA1fhJnftgdv6F59dpO1sFkqBkvn9d"


def request_animal_search(search_item):
    """
    Executes the API Search for the Search Item
    :param search_item: A string by the user
    :return: The API Output.
    """
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(search_item)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        # print(response.json())
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


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
    locations = animal["locations"]  # may result in a list
    locations = " and ".join(locations)  # makes list to a string of locations

    try:
        scientific_name = animal["taxonomy"]["scientific_name"]
    except KeyError:
        scientific_name = "Empty"

    try:
        animal_type = animal["characteristics"]["type"]
    except KeyError:
        animal_type = "Empty"

    return name, diet, locations, animal_type, scientific_name


def serialize_animal(animals_processed):
    """
    Writes the HTML for each animal.
    :param animals_processed: the 4 or 5 animal data objects from get_animal_information()
    :return: html string of the serializes animal
    """
    output_html = ''
    name, diet, locations, animal_type, scientific_name = animals_processed

    output_html += f'<li class="cards__item">\n'
    output_html += f'<div class="card__title">{name}</div>'
    output_html += f'<p class="card__text">\n'
    output_html += f'<ul class="no-bullets">\n'
    output_html += f"<li><strong>Location(s):</strong> {locations}</li>\n"

    if animal_type != "Empty":
        output_html += f"<li><strong>Type:</strong> {animal_type}</li>\n"

    output_html += f"<li><strong>Diet:</strong> {diet}</li>\n"
    output_html += f"<li><strong>Scientific Name:</strong> {scientific_name}</li>\n"
    output_html += f'</ul>\n\n'

    return output_html


def generate_html_page(user_input, animals_data):
    # animals_data = load_data(filepath)

    animal_count = len(animals_data)
    output_html = ""

    for animal_number in range(0, animal_count):
        single_animal_data = get_animal_information(animals_data, animal_number)
        output_html += serialize_animal(single_animal_data)

        with open("animals_template.html", "r") as html_file:
            template_content = html_file.read()

    # Replace the placeholder with the generated animal information
    updated_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output_html)
    output_folder = "/Users/jonashapp/Documents/GitHub/Pycharm/MS_Codio_Zootopia_With_API/RequestedAnimalWebsites/"

    # Write the updated HTML content into a new HTML file
    new_html_doc = os.path.join(output_folder, f"animals_with_api_{user_input.lower()}.html")

    with open(new_html_doc, "w") as output_file:
        output_file.write(updated_html_content)

    print(f"Website was successfully generated to the file animals_with_api_{user_input.lower()}.html")


def generate_html_page_invalid_search(user_input):

    output_html = f"<h2>No Results for {user_input}! Please try another one.</h2>\n"

    with open("animals_template.html", "r") as html_file:
        template_content = html_file.read()

    # Replace the placeholder with the generated animal information
    updated_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output_html)
    output_folder = "/Users/jonashapp/Documents/GitHub/Pycharm/MS_Codio_Zootopia_With_API/RequestedAnimalWebsites/"

    # Write the updated HTML content into a new HTML file
    new_html_doc = os.path.join(output_folder, f"animals_with_api_invalid_search.html")

    with open(new_html_doc, "w") as output_file:
        output_file.write(updated_html_content)

    print(f"Website was successfully generated to the file animals_with_api_invalid_search.html")


def main():
    """
    Gets the user input until a search query with valid results is found.
    Executes the Data Prep Functions and passes them to the HTML Writing Functions.
    :return: Nothing. HTML ist written in another function.
    """

    is_not_valid_animal = True

    while is_not_valid_animal:

        user_request = str(input("Please ask for an animal: "))
        animals_data = request_animal_search(user_request)

        if not animals_data:
            print(f"No Animal with the name {user_request} could be found! Please try another one.\n")
            generate_html_page_invalid_search(user_request)
            continue
        else:
            generate_html_page(user_request, animals_data)
            is_not_valid_animal = False


if __name__ == "__main__":
    main()

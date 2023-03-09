def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max_in_list(list_of_numbers):
    max_number = list_of_numbers[0]
    for number in list_of_numbers:
        if max_number < number:
            max_number = number
    return max_number

def sort_dictionary(d):

    sorted_by_age = sorted(d.items(), key=lambda x: x[1][1])

    result = [(name, phone) for name, (phone, age) in sorted_by_age]

    return result


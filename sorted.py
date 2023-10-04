def sort_dictionary(input_dict):
  
    sorted_dict = dict(sorted(input_dict.items()))

 
    sorted_list = [(name, info[0]) for name, info in sorted_dict.items()]

    return sorted_list

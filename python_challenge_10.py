import itertools

a = ["1", "11", "21", "1211", "111221"]
# '
def look_and_say(length):
    mapper = {
       ("1",): "11",
       ("1", "1"): "21",
       ("1", "1", "1"): "31",
       ("2", "2", "2"): "32",
       ("2", "2"): "22",
       ("2",): "12",
       ("3", "3", "3"): "33",
       ("3", "3"): "23",
       ("3",): "13"} 
 
    previous_string = "1"
    result_array = list(previous_string)
    for i in xrange(length-1):
        new_sequence = [mapper[tuple(substring)] for character, substring in itertools.groupby(previous_string)]
        new_string = "".join(new_sequence)
        previous_string = new_string
        result_array.append(new_string)
    return result_array

result = look_and_say(31)
print "{}: {}".format(len(result[30]), result[30])
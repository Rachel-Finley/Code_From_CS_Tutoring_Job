'''
Three variables,  x , y and  z , supposedly hold strings of digits, suitable for converting to integers.
Write code that converts these to integers and print the sum of these three integers. However, if any variable
has a value that cannot be converted to an integer, print out, the string "bad value(s) in:
"followed by the names of the variables that have bad values (separated by spaces, in alphabetically
ascending order).

For example, if the values of x, y and z were respectively "3", "9", "2" then the number 14 would be
printed; but if the values were "abc", "15", "boo" then the output would be: bad value(s) in: x z

Since we need to 'catch' runtime errors of each conversion on each variable,
we need to convert and add one variable at a time. That means accumulate the conversion
of one variable at a time in its own try statement. If an error occurs, add some text
to a variable that we will be printed at the end.
'''
import re

def convert_to_int(variable_1, variable_2, variable_3):
    return int(variable_1), int(variable_2), int(variable_3)


def main():
    x = "15"
    y = "88"
    z = "24a"

    try:
        x, y, z = convert_to_int(x, y, z)

    except ValueError:
        test_list = [x, y, z]
        placeholder_list = []
        for item in test_list:
            for item_2 in re.split(r"\D", item):
                placeholder_list.append(item_2)


    print(placeholder_list.remove(""))

main()


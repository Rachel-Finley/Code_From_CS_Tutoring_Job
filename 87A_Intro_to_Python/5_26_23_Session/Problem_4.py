def main():
    solution = 0
    num = input("Enter a number to divide 10 by: ")

    try:
        # try first to convert user's input into an integer
        num = int(num)
        # If we are able to, calculate solution
        solution = 10.0 / num


    except ValueError:
        # Check if the datatype is a string first
        if type("") == type(num):

            # try then to convert to a float
            try:
                num = float(num)
                solution = 10.0 / num

            # If its not a float, tell user to enter number
            except ValueError:
                print("You entered a string. Please use a number.")

            # check for 0.0 zero division error with floats
            except ZeroDivisionError:
                print("Can't divide by 0")

            # handle any unknown errors
            except:
                print("An unknown error has occured.")

    # check for 0 zero division error with integers
    except ZeroDivisionError:
        print("Can't divide by 0")

    # handle unknown cases
    except:
        print("An unknown error has occured.")

    # if either a integer or string was provided
    # print results of whichever one worked using an "f-string"
    finally:
        print(f"The solution is: {solution}")


# Run the main function
main()

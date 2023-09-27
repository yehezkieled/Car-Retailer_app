# import libraries
import os
import random
import re
import string
import time

# import classes
from car import Car
from car_retailer import CarRetailer


# function to display main menu
def main_menu():
    """
    show the main menu

    Returns
    ----------
    none
    """

    print("Welcome to the Car Purchase Advisor System.")
    print("------------------------")
    print("1. Look for the nearest car retailer")
    print("2. Get car purchase advice")
    print("3. Place a car order")
    print("4. Exit")
    print("Input 0, to go back to main menu.")
    print("------------------------")


def sub_menu(car_retailer_obj):
    """
    show the sub main menu for option 2

    Returns
    ----------
    none
    """

    print("------------------------")
    print("Thank you for picking, ", car_retailer_obj.retailer_name)
    print("------------------------")
    print("Please select the menu below. ")
    print("i)     Recommend  car")
    print("ii)    Get all cars in stock")
    print("iii)   Get cars in stock by car types (e.g., [“AWD”, “RWD”])")
    print("iv)    Get probationary licence permitted cars in stock")
    print("e.g. answer: 'iv'. ")


def print_car_info(car_obj):
    """
    print the car object info

    Returns
    ----------
    none
    """

    # get per car information by using the str method on the car object
    per_car_info = str(car_obj)
    # split the str to access the information
    per_car_info_list = per_car_info.split(", ")

    # print the information of the car
    print("Car name                 : ", per_car_info_list[1])
    print("Car code                 : ", per_car_info_list[0])
    print("Car capacity             : ", per_car_info_list[2])
    print("Car horsepower           : ", per_car_info_list[3])
    print("Car weight               : ", per_car_info_list[4])
    print("Car type                 : ", per_car_info_list[5])
    print("------------------------\n")


# function to change time format
def change_time(business_time):
    """
    change the business hour format

    Returns
    ----------
    open_time : str
        reformatted time
    close_time : str
        reformatted time
    """

    # get the hour from the open business hour
    open_hour = int(business_time[0])
    # get the min from the open business hour
    open_min = int((business_time[0] - open_hour) * 60)

    # getting the open time
    open_time = f"{open_hour:02d}:{open_min:02d}"

    # get the hour from the close business hour
    close_hour = int(business_time[1])
    # get the min from the close business min
    close_min = int((business_time[1] - close_hour) * 60)

    # getting the close time
    close_time = f"{close_hour:02d}:{close_min:02d}"

    return open_time, close_time


# function to generate test data
def generate_test_data():
    """
    generate stock txt data

    Returns
    ----------
    none
    """

    # data folder path
    data_dir = "data"
    # checking whether the data folder exists
    if not os.path.exists("../" + data_dir):
        # if not, create the folder
        path = os.path.join("../", data_dir)
        os.mkdir(path)

    # write empty stock txt file and order txt file
    with open("../data/stock.txt", "w") as file:
        pass

    with open("../data/order.txt", "w") as file:
        pass

    # required number of retailer and their stock cars
    num_of_retailer = 3
    num_of_car_per_retailer = 4

    # list to store retailer object
    retailer_obj_list = []

    # attributes list, to make sure that there are not double value for each retailer
    retailer_id_list = []
    retailer_name_list = []
    car_code_list = []
    car_name_list = []

    # available choice for few attributes
    retailer_address_choices = [
        "Wellington Road Clayton, VIC3800",
        "Morton Street Clayton, VIC3169",
        "Dandenong Road Clayton, VIC3128",
        "Royalty Street Clayton, VIC3158",
        "Kionga Street Clayton, VIC3148",
        "Alice Street Clayton, VIC3850",
        "Atlantic Street Clayton, VIC3168"
    ]
    car_type_choices = ["RWD", "AWD", "FWD"]

    # for loop to create CarRetailer object
    for per_retailer in range(num_of_retailer):

        # pattern of the regex for the retailer_name
        pattern_name = r"^[a-zA-Z\s]{10}$"
        # while statement to check whether the name is already in used and the new name is align with the pattern
        while True:
            # create retailer_name using the list of comprehension
            retailer_name = "".join(random.choice(string.ascii_letters + ' ') for ltr in range(10))
            # if match the pattern and not in the retailer_name_list
            if re.match(pattern_name, retailer_name):
                if retailer_name not in retailer_name_list:
                    break

        # appending the new name into the retailer_name_list
        retailer_name_list.append(retailer_name)

        # choosing one of the available addresses
        retailer_address = random.choice(retailer_address_choices)

        # determine the open hour of the retailer
        retailer_business_hour_start_time = round(random.uniform(6, 12), 1)
        # creating a touple and set the close hour of the retailer according to the open hour
        retailer_business_hour = (
            retailer_business_hour_start_time,
            round(random.uniform(retailer_business_hour_start_time + 6, 23), 1)
        )

        # creating CarRetailer object
        retailer_obj = CarRetailer(
            retail_id=-1,
            retailer_name=retailer_name,
            carretailer_address=retailer_address,
            carretailer_business_hours=retailer_business_hour,
            carretailer_stock=[]
        )

        # generate the retailer_id of the retailer_obj
        retailer_obj.generate_retailer_id(retailer_id_list)

        # appending the new id into the retaielr_id_list
        retailer_id_list.append(retailer_obj.retailer_id)

        # appending the new CarRetailer obj into the retailer_obj_list
        retailer_obj_list.append(retailer_obj)

    # create a string to be written into the stock.txt
    stock_str = "\n".join(str(per_retailer_obj) for per_retailer_obj in retailer_obj_list)

    # create a stock.txt file and write stock_str inside
    with open("../data/stock.txt", "w") as file:
        # write the file
        file.write(stock_str)

    # for looping the retailer obj
    for retailer_obj in retailer_obj_list:
        # for loop to create car objects
        for per_car in range(num_of_car_per_retailer):
            # pattern of the regex for the car_code
            pattern_car_code = r"^[A-Z]{2}\d{6}$"
            # while statement to check whether the car_code is matching the pattern and unique
            while True:
                # create the first 2 letters
                letters = "".join(random.choice(string.ascii_uppercase) for ltr in range(2))
                # create the remaining 6 digits
                digit = "".join(str(random.randint(0, 9)) for dgt in range(6))
                # combining the letters and digits
                car_code = letters + digit
                # if match the pattern and not in the car_code_list then exit the loop
                if re.match(pattern_car_code, car_code):
                    if car_code not in car_code_list:
                        break

            # appending the new car_code into the list
            car_code_list.append(car_code)

            # patter of the regex for the car_name
            patter_car_name = r"^[a-zA-Z\s]{10}$"
            # while statement to check whether the name is the same as the pattern and unique
            while True:
                # create car name
                car_name = "".join(random.choice(string.ascii_letters + ' ') for ltr in range(10))
                # if matches and not in the list then exit the loop
                if re.match(patter_car_name, car_name):
                    if car_name not in car_name_list:
                        break

            # append the new car_name into the list
            car_name_list.append(car_name)

            # create car capacity
            car_capacity = random.randint(5, 20)

            # create car horse power
            car_horse_power = random.randint(100, 200)

            # create car_weight
            car_weight = random.randint(1500, 3000)

            # choosing one car type from the avaialable choice
            car_type = random.choice(car_type_choices)

            # create car object
            car_obj = Car(
                car_code,
                car_name,
                car_capacity,
                car_horse_power,
                car_weight,
                car_type
            )

            # add the car object to the CarRetailer_obe
            retailer_obj.add_to_stock(car_obj)


# function to declare the objects
def declare_obj():
    """
    declare all car retailer objects

    Returns
    ----------
    car_retailer_object_list : list
        list containing car retailer objects
    """

    # generate random test data
    generate_test_data()

    # get the directory of the file
    dir_file = os.getcwd()
    # split the dir_file string
    list_folders = dir_file.split("/")
    # erase the last element of the lest
    list_folders.pop()
    # rejoin the directory
    parent_dir = "/" + "/".join(list_folders)
    # append the folder name
    dir_data = parent_dir + "/data"
    # append the file name
    stock_txt_dir = dir_data + "/stock.txt"

    # open the txt file using the path provided
    with open(stock_txt_dir, "r") as file:
        stock_txt = file.read()

    # store it into lists for retailer
    retailer_car_info = stock_txt.split("\n")

    # create a list to store the car retailer object
    car_retailer_object_list = []
    # for loops to get the car_code data to be stored inside the carretailer_stock variable
    for per_retailer in retailer_car_info:
        # split into 2 list, retailer info and their car info
        retailer_car_info_list = per_retailer.split("[")

        # seperate the list
        retailer_info = retailer_car_info_list[0]
        retailer_info_list = retailer_info.split(", ")

        # getting the business hour variable for the retailer
        business_hours = retailer_info[
                         retailer_info.index("(") + 1: retailer_info.index(")")
                         ]
        # convert is to tuple
        business_hours = tuple(
            [float(hour) for hour in business_hours.split(", ")]
        )

        # create retailer object to store in the retailer_object_list
        car_retailer_object_list.append(CarRetailer(
            retail_id=int(retailer_info_list[0]),
            retailer_name=retailer_info_list[1],
            carretailer_address=", ".join(retailer_info_list[2:4]),
            carretailer_business_hours=business_hours,
            carretailer_stock=[]
        ))

    # creating car objects to be stored in the car_retailer
    for per_retailer_obj_index in range(len(car_retailer_object_list)):
        car_retailer_object_list[per_retailer_obj_index].load_current_stock(stock_txt_dir)

    # returning the car_retailer_object_list
    return car_retailer_object_list


def main():
    """
    run the whole system application

    Returns
    ----------
    none
    """

    # invoking the car_retailer_object_list to get the CarRetailer objects
    car_retailer_object_list = declare_obj()

    # while the program is True, it keeps on running
    while True:
        # invoking the main_menu function
        main_menu()

        # while true, keep on asking to give the correct input
        while True:
            # try the input
            try:
                # asking for the user input
                user_input = int(input("Please input an option: "))
                # making sure that the input is within the main_menu option:
                while True:
                    # if it is inbetween the range exit the loop
                    if 0 < user_input <= 4:
                        break
                    # reasking the user_input
                    print("Please input the the option between 1 and 4.")
                    user_input = int(input("Please input an option: "))
            # valueError exception
            except ValueError:
                # reasking the input
                print("Please input the a digit.")
                continue
            # break the loop
            break

        # if the user input is 1, return the nearest car retailer
        if user_input == 1:

            # while true, keep on asking to give the correct input
            while True:
                # try the input
                try:
                    # asking fot the postcode input of the user
                    user_postcode = int(input("Please enter your postcode (4 digits): "))

                    # 4 digit regex pattern
                    pattern = "^\d{4}$"
                    # making sure that the input is 4 digit:
                    while True:
                        # if the user wants to go back
                        if user_postcode == 0:
                            break

                        # if the user_postcode is the same as pattern then exit the loop
                        if re.match(pattern, str(user_postcode)):
                            break
                        # reasking the input
                        print("Please enter a 4 digits postcode e.g. '1234'. ")
                        user_postcode = int(input("Please enter your postcode (4 digits): "))
                # ValueError exception
                except ValueError:
                    # reasking the input
                    print("Please only enter digits. ")
                    continue
                # break the loop
                break

            if user_postcode != 0:
                # empty list to store the difference of all postcode
                postcode_diff_list = []
                # for loops to check which retailer is the nearest
                for per_retailer in car_retailer_object_list:
                    postcode_diff_list.append(per_retailer.get_postcode_distance(user_postcode))

                # min value of postcode
                min_value_diff = min(postcode_diff_list)

                # empty list to store possible several min_value_postcode
                nearest_retailer_list = []
                # enumerate for loops incase there are 2 near retailer
                for ind, value in enumerate(postcode_diff_list):
                    # if the value is the minimum then append to the list
                    if value == min_value_diff:
                        nearest_retailer_list.append(car_retailer_object_list[ind])
                # select a random retailer among the choice
                nearest_retailer = random.choice(nearest_retailer_list)

                # reformat the business hour into more familiar format
                open_time, close_time = change_time(nearest_retailer.carretailer_business_hours)

                print("Below the detail of the nearest retailer from your location.")
                print("Retailer name            : ", nearest_retailer.retailer_name)
                print("Retailer id              : ", nearest_retailer.retailer_id)
                print("Retailer address         : ", nearest_retailer.carretailer_address)
                print("Retailer operating hour  : ", open_time, "-", close_time)
                print("Cars in stock            : ",
                      str([per_car.car_code for per_car in nearest_retailer.get_all_stock()]))

        # if the user input is 2
        if user_input == 2:
            # print instruction
            print("Choose one of the retailer below:")
            print("--------------------------------")

            # create an empty list to store the retailer_id
            retailer_id_list = []

            # for looping the list of car retailer:
            for per_retailer in car_retailer_object_list:
                # reformat the buseiness hour into more familiar format
                open_time, close_time = change_time(per_retailer.carretailer_business_hours)

                # printing the information
                print("Retailer name            : ", per_retailer.retailer_name)
                print("Retailer id              : ", per_retailer.retailer_id)
                print("Retailer address         : ", per_retailer.carretailer_address)
                print("Retailer operating hour  : ", open_time, "-", close_time)
                print("----------------------------")

                # appending the retailer_id into the list
                retailer_id_list.append(per_retailer.retailer_id)

            # while true, keep on asking to give the correct input
            while True:
                # try the input
                try:
                    retailer_id_input = int(input("Please input the retailer's id: "))

                    # making sure that the user input the correct input
                    while True:
                        # if the user wants to go back
                        if retailer_id_input == 0:
                            break

                        # if the input id is in the list then exit loop
                        if retailer_id_input in retailer_id_list:
                            break
                        # reasking the input
                        print("Please input the correct retailer id. ")
                        retailer_id_input = int(input("Please input the retailer's id: "))
                # ValueError exception
                except ValueError:
                    # reasking the input
                    print("Please input the correct retailer id. ")
                    continue
                # break the loop
                break

            # if the user wants to go back
            if retailer_id_input != 0:
                # defining selected car retailer
                selected_car_retailer = car_retailer_object_list[retailer_id_list.index(retailer_id_input)]

                # invoking the sub_menu function
                sub_menu(selected_car_retailer)

                # asking the user for the input
                sub_menu_input = input("Please input the option: ")

                # regex pattern
                pattern = r"^(i{1,3}|iv)$"
                # making sure that the input is valid
                while True:
                    # if the user wants to go back
                    if sub_menu_input == "0":
                        break

                    # if the sub_menu_input matches the patter, exit loop
                    if re.match(pattern, sub_menu_input):
                        break
                    # reasking to input the correct sub menu
                    print("Please input the correct format, e.g. 'iii' ")
                    sub_menu_input = input("Please input the option: ")

                # if the user wants to go back
                if sub_menu_input != "0":
                    # recommend a car
                    if sub_menu_input == 'i':
                        # get a random car from the car_recommendation() method
                        random_car_obj = selected_car_retailer.car_recommendation()

                        # print the information of the retailer and the car
                        print("------------------------")
                        print("Below are the information for the recommended stock. ")
                        print("Retailer name            : ", selected_car_retailer.retailer_name)
                        print("Retailer id              : ", selected_car_retailer.retailer_id)

                        # invoke the random_car_obj to print the car info
                        print_car_info(random_car_obj)

                    # get all cars in stock
                    if sub_menu_input == 'ii':
                        # getting the available car for the selected car retailer using the get_all_stock() method
                        available_car_obj_list = selected_car_retailer.get_all_stock()

                        # printing all the information of the retailer and the car
                        print("------------------------")
                        print("Below are the information for the available stock for the selected car retailer. ")
                        print("Retailer name            : ", selected_car_retailer.retailer_name)
                        print("Retailer id              : ", selected_car_retailer.retailer_id)
                        print("------------------------\n\n")

                        # for looping each car to get the information
                        for per_car in available_car_obj_list:
                            # invoke the print_car_info to print the car object information
                            print_car_info(per_car)

                    # get cars in stock by car types
                    if sub_menu_input == 'iii':
                        # the available car types
                        car_type_choices = ["RWD", "AWD", "FWD"]
                        # telling the user the available car types
                        print("Below are the available car types we have, \n", str(car_type_choices))

                        # making sure the input is correct:
                        while True:
                            # asking for the input of the user on which car type they want
                            car_type_selected = (input("Please input the car type: ")).upper().strip()

                            # if the user wants to go back
                            if car_type_selected == "0":
                                break

                            # if the car_type_selected not in the available list
                            if car_type_selected in car_type_choices:
                                break
                            # reasking the input
                            print("Please input the correct car type. ")

                        if car_type_selected != "0":
                            # getting the car list using the get_stock_by_car_type() method
                            car_by_types_list = selected_car_retailer.get_stock_by_car_type(car_type_selected)

                            # printing all the information of the retailer and the car
                            print("------------------------")
                            print("Below are the information for the available stock for the selected car retailer. ")
                            print("Retailer name            : ", selected_car_retailer.retailer_name)
                            print("Retailer id              : ", selected_car_retailer.retailer_id)
                            print("------------------------\n")

                            # if there are no car types like this
                            if not car_by_types_list:
                                print("There are no car with ", car_type_selected, " type.")
                                print("------------------------\n")
                            else:
                                # for looping each car to get the information
                                for per_car in car_by_types_list:
                                    # invoke the print_car_info to print the car object information
                                    print_car_info(per_car)

                    # get probationary licence car
                    if sub_menu_input == 'iv':
                        # define the license_type
                        license_type = ["L", "P", "Full"]
                        # telling the user the available car types
                        print("Below are the available license type we support, \n", str(license_type))

                        # making sure that the license input is available
                        while True:
                            # ask the user for their license type
                            user_license_input = input("Please input your license type: ").upper().strip()

                            # if the user wants to go back to main menu
                            if user_license_input == "0":
                                break

                            # if the license type is supported then exit loop
                            if user_license_input in license_type:
                                break
                            # reasking for the correct input
                            print("Please input the correct license input. ")

                        if user_license_input != 0:
                            # getting the car list using the get_stock_by_license_type method
                            car_probationary_selected = selected_car_retailer.get_stock_by_licence_type(user_license_input)

                            # printing all the information of the retailer and the car
                            print("------------------------")
                            print("Below are the information for the available stock for the selected car retailer. ")
                            print("Retailer name            : ", selected_car_retailer.retailer_name)
                            print("Retailer id              : ", selected_car_retailer.retailer_id)
                            print("------------------------\n")

                            # check if there is a car in the list or not
                            if not car_probationary_selected:
                                print("There are no probationary car. ")
                            else:
                                # for looping each car to get the information
                                for per_car in car_probationary_selected:
                                    # invoke the print_car_info to print the car object information
                                    print_car_info(per_car)

        # if the user input is 3
        if user_input == 3:
            # empty lists to store the list of car codes and retailer ids
            retailer_id_list = []
            car_code_list = []

            # getting the list of the available car retailer id
            for per_retailer in car_retailer_object_list:
                # appending each retailer id into the list
                retailer_id_list.append(per_retailer.retailer_id)

            # making sure that the input is correct
            while True:
                # try the input
                try:
                    # asking for the user for the input
                    user_order_input = input(
                        "Please input the selected retailer id and car codes. (format: 'retailer_id  "
                        "car_code'): ")

                    # making sure the input is correct
                    while True:
                        # if the user wants to go back
                        if user_order_input == "0":
                            break
                        # split the input string
                        user_order_input_list = user_order_input.split(" ")
                        # separate it into different variable
                        user_order_input_retailer_id = int(user_order_input_list[0])
                        user_order_input_car_codes = user_order_input_list[1]
                        # if the restailer in the retailer id list
                        if user_order_input_retailer_id in retailer_id_list:
                            selected_retailer = car_retailer_object_list[retailer_id_list.index(user_order_input_retailer_id)]
                            if (user_order_input_car_codes in selected_retailer.carretailer_stock) or selected_retailer.carretailer_stock == []:
                                break
                        print("Please input the correct retailer id and car codes format. (e.g. '67288439 "
                              "ZN430217')")
                        # asking for the user for the input
                        user_order_input = input(
                            "Please input the selected retailer id and car codes. (format: 'retailer_id  "
                            "car_code'): ")
                # if the error is IndexError
                except IndexError:
                    print("Please input the correct retailer id and car codes format. (e.g. '67288439 ZN430217')")
                    continue
                # if the error is ValueError
                except ValueError:
                    print("Please input the correct retailer id and car codes format. (e.g. '67288439 ZN430217')")
                    continue
                break

            # if the user wants to go back
            if user_order_input != "0":
                # getting the selected retaier
                if selected_retailer.carretailer_stock:

                    # getting the current time
                    curr_time = time.localtime()
                    # getting the hour and minutes
                    curr_hour = curr_time.tm_hour
                    curr_minute = curr_time.tm_min
                    # getting the float time of the current time
                    curr_time_float = curr_hour + round(curr_minute / 60, 1)

                    # if statement to check whether the current time is within the business hour using the
                    # is_operating() method
                    if selected_retailer.is_operating(curr_time_float):
                        # create a new order using the create_order() method
                        new_order = selected_retailer.create_order(user_order_input_car_codes)

                        # getting the order information
                        new_order_str = str(new_order)
                        # split the str to get access to the informatioin
                        new_order_list = new_order_str.split(", ")

                        # print the order information
                        print("------------------------")
                        print("Order id             : ", new_order_list[0])
                        print("Order car code       : ", new_order_list[1])
                        print("From retailer        : ", new_order_list[2])
                        print("Order creation time  : ", time.ctime())
                        print("------------------------")
                    else:
                        # if not between the operating hour, tell the user to pick other retailer
                        print("------------------------")
                        print("Please pick other car retailer, because the car retailer is closed during this time.")

                        # reformat the business hour into more familiar format
                        open_time, close_time = change_time(selected_retailer.carretailer_business_hours)

                        # print the open and close time information to inform the user
                        print("This retailer will open tomorrow at {} and will close at {}.".format(open_time, close_time))
                        print("------------------------")
                else:
                    print("The retailer is out of stock.")

        # if the user input is 4
        if user_input == 4:
            # print thank you
            print("Thank you for using our services.\nHave a nice day!")
            # exit the loop
            break


# invoking the main function
if __name__ == "__main__":
    main()

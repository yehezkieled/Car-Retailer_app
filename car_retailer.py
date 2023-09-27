# import libraries
import random
import time
import re

# import classes
from car import Car
from retailer import Retailer
from order import Order


# create CarRetailer class
class CarRetailer(Retailer):
    """
    A class used to represent an Order


    Attributes
    ----------
    retailer_id : str
        a string to store the retailer's id
    retailer_name : str
        a string to store the retailer's name
    carretailer_address : str
        a string to store the retailer's address
    carretailer_business_hours : tuple
        a tuple to store the retailer's business hour
    carretailer_stock : list
        a list to store the car stock that the retailer have

    Methods
    -------
    __str__()
        Return the car retailer information as a formatted string
    load_current_stock()
        loading the folder path to extract the car code information
    is_operating()
        to check whether the retailer is still open
    get_all_stock()
        get all the car object stock for the retailer
    get_postcode_distance()
        get the distance between the user and the retailer's postcode
    remove_from_stock()
        remove a car object in the system
    add_to_stock()
        add a car object to the system
    get_stock_by_car_type()
        filter car objects by the car type
    get_stock_by_licence_type()
        filter the car objects by the licence type
    car_recommendation()
        recommend a random car object
    create_order()
        create order by calling the order class
    """

    # declaring the class attributes
    def __init__(self,
                 retail_id=88727858,
                 retailer_name="dLrIrEaovi",
                 carretailer_address="Wellington Rd Clayton, VIC3168",
                 carretailer_business_hours=(8.8, 14.2),
                 carretailer_stock=[]):
        """
        Parameters
        ----------
        retailer_id : str
            a string to store the retailer's id (default value is 12345678)
        retailer_name : str
            a string to store the retailer's name (default value is "Halo")
        carretailer_address : str
            a string to store the retailer's address (default value is "Wellington Rd Clayton, VIC3168")
        carretailer_business_hours : tuple
            a tuple to store the retailer's business hour (default value is (8.8, 14.2))
        carretailer_stock : list
            a list to store the car stock that the retailer have (default value is [])
        """

        super().__init__(retail_id, retailer_name)
        self.carretailer_address = carretailer_address
        self.carretailer_business_hours = carretailer_business_hours
        self.carretailer_stock = carretailer_stock

    # create print function
    def __str__(self):
        """
        generate the car retailer information as a formatted string

        Returns
        ----------
        str
            the car retailer object information.
        """

        # returning the joined attribute
        return ", ".join([
            str(self.retailer_id),
            str(self.retailer_name),
            str(self.carretailer_address),
            str(self.carretailer_business_hours),
            str(self.carretailer_stock)
        ])

    # this function needs to be checked
    def load_current_stock(self, path):
        """
        load a directory to get the car codes filtered by the retailer's id

        Returns
        ----------
        none
        """

        # open the txt file using the path provided
        with open(path, "r") as file:
            stock_txt = file.read()

        # split into lists for retailer
        retailer_car_info = stock_txt.split("\n")

        # for loops to get the car_code data to be stored inside the carretailer_stock variable
        for per_retailer in retailer_car_info:
            # split into 2 list, retailer info and their car info
            retailer_car_info_list = per_retailer.split("[")

            # seperate the list
            retailer_info = retailer_car_info_list[0]
            # make retailer_info into list
            retailer_info_list = retailer_info.split(", ")

            # if statement to get the car_codes for a particular retailer
            if int(retailer_info_list[0]) == self.retailer_id:

                # take the car_info
                car_info = retailer_car_info_list[1][:-1]
                # split the car_info into n cars which the retailer sell.
                car_info_list = car_info.split("', ")

                # for looping the car_info_list to clean the data and get the list of info for each car
                for per_car_index in range(len(car_info_list)):
                    car_info_list[per_car_index] = car_info_list[per_car_index].strip("'")
                    car_info_list[per_car_index] = car_info_list[per_car_index].split(", ")

                # store it into the self.carretailer_stock
                for per_car in car_info_list:
                    self.carretailer_stock.append(per_car[0])

    # this function needs to be checked
    def is_operating(self, cur_hour):
        """
        to determine whether a retailer is still open or not.

        Returns
        ----------
        bool
            return True if it is open.
        """

        return self.carretailer_business_hours[0] <= cur_hour <= self.carretailer_business_hours[1]

    # create a function to get all car object stock for a particular retailer
    def get_all_stock(self):
        """
        get all car object from the txt file filtered by the retailer's id

        Returns
        ----------
        list
            list of car object.
        """

        # create an empty list
        car_obj_list = []

        # open the stock txt file
        with open("../data/stock.txt", "r") as file:
            # store value line in a list
            stock_txt_list = file.readlines()

        # for looping the line
        for per_line in stock_txt_list:
            # if the line is the retailer's then create car objects
            if int(per_line[:8]) == self.retailer_id:
                # regex pattern to get the car
                pattern_line = r"'(.*?)'"
                # getting all the car
                car_list = re.findall(pattern_line, per_line)
                # looping the list and create car object
                for per_car_str in car_list:
                    # split every element in the str to get the car info
                    per_car_info_list = per_car_str.split(", ")
                    # create car object
                    car_obj = Car(
                        per_car_info_list[0],
                        per_car_info_list[1],
                        per_car_info_list[2],
                        per_car_info_list[3],
                        per_car_info_list[4],
                        per_car_info_list[5]
                    )
                    # appending the car object to the list
                    car_obj_list.append(car_obj)

        # returning the car_obj_list
        return car_obj_list

    # function to get the absolute distance from the postcode
    def get_postcode_distance(self, postcode):
        """
        get the distance between postcode

        Returns
        ----------
        int
            the distance between the user and the retailer's postcode.
        """

        # returning the absolute distance of the postcode
        return abs(postcode - int(self.carretailer_address[-4:]))

    # function to remove a car object and car_code from the global variable and the self.carretaielr_stock
    def remove_from_stock(self, car_code):
        """
        remove a car object from the stock txt file filtered by car code and retailer's id

        Returns
        ----------
        bool
            return True if the remove is successful.
        """

        # to check whether the car_code is in the self.carretailer_stock
        if car_code in self.carretailer_stock:
            # remove the car_code inside the self.carretailer_stock
            self.carretailer_stock.remove(car_code)

            stock_car = []
            for per_car in self.get_all_stock():
                if per_car.car_code in self.carretailer_stock:
                    stock_car.append(per_car)

            # create a str by printing all car object for a particular retailer
            stock_list = [str(car_obj) for car_obj in stock_car]

            # open the file to read
            with open("../data/stock.txt", "r") as file:
                # creating list of text per line
                stock_txt_list = file.readlines()

            # for looping the stock_txt_list
            for per_retailer_index in range(len(stock_txt_list)):
                # trimming the "\n"
                stock_txt_list[per_retailer_index] = stock_txt_list[per_retailer_index].strip("\n")
                # checking retailer_id if it is the same
                if int(stock_txt_list[per_retailer_index][:8]) == self.retailer_id:
                    # getting the "[" index
                    list_index = stock_txt_list[per_retailer_index].index("[")
                    # only take the retailer info
                    new_str = stock_txt_list[per_retailer_index][:list_index]
                    # appending the stock str
                    new_str += str(stock_list)
                    # replacing the current index value
                    stock_txt_list[per_retailer_index] = new_str

            # open the file to write
            with open("../data/stock.txt", "w") as file:
                # writing the file
                file.write("\n".join(stock_txt_list))

            # returning True if it is removed
            return True

        # returning False
        return False

    # this function might be needed to be connected to the Car class somehow
    def add_to_stock(self, car):
        """
        add a car object into the stock txt filtered by retailer's id

        Returns
        ----------
        bool
            return True if the add successful.
        """

        # if the car_code not in the self.carretailer_stock
        if car.car_code not in self.carretailer_stock:
            # appending the car_code inside the self.carretailer_stock
            self.carretailer_stock.append(car.car_code)

            # open the stock.txt file to read
            with open("../data/stock.txt", "r") as file:
                stock_txt_list = file.readlines()

            # looping the txt_file
            for per_retailer_index in range(len(stock_txt_list)):
                # trimming the "\n"
                stock_txt_list[per_retailer_index] = stock_txt_list[per_retailer_index].strip("\n")
                # if the retailer_id is the same then replace the line
                if int(stock_txt_list[per_retailer_index][:8]) == self.retailer_id:
                    # creating new_line by appending the car object
                    new_line = stock_txt_list[per_retailer_index][:-1]
                    if new_line[len(new_line) - 1] == "[":
                        new_line += "'"
                        new_line += str(car)
                    else:
                        new_line += ", '"
                        new_line += str(car)
                    new_line += "']"
                    # replacing the old line
                    stock_txt_list[per_retailer_index] = new_line

            # write the file
            with open("../data/stock.txt", "w") as file:
                file.write("\n".join(stock_txt_list))

            # return True if to write is successful
            return True

        # return False
        return False

    # function to get car stock by car_type for a particular retailer
    def get_stock_by_car_type(self, car_types):
        """
        filter the car stock by car type

        Returns
        ----------
        list_car_obj : list
            list of car object.
        """

        # empty list to store the car object
        list_car_obj = []

        # for looping the car that the retailer have in stock
        for car_obj in self.get_all_stock():
            # if the car type object is the same as required
            if car_obj.get_car_type() == car_types:
                # append to the list_car_obj if the same
                list_car_obj.append(car_obj)
        # return the list_car_obj
        return list_car_obj

    # function to get car stock by licence type for a particular retailer
    def get_stock_by_licence_type(self, licence_type):
        """
        filter the car stock by license type

        Returns
        ----------
        list_car_obj : list
            list of car object.
        """

        # if the licence is equal to "P" then proceed
        if licence_type == "P":
            # empty list to store the car object
            list_car_obj = []

            # for looping the car that the retailer have in stock
            for car_obj in self.get_all_stock():
                # if not the probationary then append to the list
                if not car_obj.probationary_licence_prohibited_vehicle():
                    list_car_obj.append(car_obj)

            # return the list
            return list_car_obj

        # if the license type is "L" and "FULL", there are no restriction
        return self.get_all_stock()

    # function to recommend a car
    def car_recommendation(self):
        """
        pick a random car object from the stock

        Returns
        ----------
        car object
            a random car object.
        """

        # return the random car object from the retailer stock
        return random.choice(self.get_all_stock())

    # function to create an order
    def create_order(self, car_code):
        """
        create an order object filtered using the car_code

        Returns
        ----------
        order_obj : order object
            order object.
        """

        # create an empty car object
        selected_car_obj = Car()
        # if the car_code in the self.carretailer_stock we put the selected car obj into the empty obj
        if car_code in self.carretailer_stock:
            # for looping the cat object that the retailer have in stock
            for car_obj in self.get_all_stock():
                # if found matching car then select the car obj to be put into the selected_car_obj
                if car_obj.found_matching_car(car_code):
                    selected_car_obj = car_obj
                    break

        # if successfully removed then create order object
        if self.remove_from_stock(car_code):
            # create order object
            order_obj = Order(
                order_car=selected_car_obj,
                order_retailer=Retailer(
                    retailer_id=self.retailer_id,
                    retailer_name=self.retailer_name
                ),
                order_creation_time=int(time.time())
            )

            # generate order id for the order object
            order_obj.generate_order_id(car_code)

            # openn the order file and read the text
            with open("../data/order.txt", "r") as file:
                order_txt_str = file.read()

            # create order txt list
            order_txt_list = order_txt_str.split("\n")
            # append the new order object into the list
            order_txt_list.append(str(order_obj))

            # if the first index is empty then pop
            if order_txt_list[0] == "":
                order_txt_list.pop(0)

            # create an str from the order_txt_list
            order_str = "\n".join(order_txt_list)

            # open the order file and write the object
            with open("../data/order.txt", "w") as file:
                file.write(order_str)

            # return the order object
            return order_obj

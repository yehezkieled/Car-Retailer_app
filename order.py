# import libraries
import random
import string

# import classes
from car import Car
from retailer import Retailer


# create Order class
class Order:
    """
    A class used to represent an Order


    Attributes
    ----------
    order_id : str
        a string to store the order's id
    order_car : Car object
        a car object
    order_retailer : Retailer object
        a retailer object
    order_creation_time : int
        an int to store the time of the creation of the order object

    Methods
    -------
    __str__()
        Return the order information as a formatted string
    generate_order_id()
        return a random order id
    """

    # declaring the class attributes
    def __init__(self,
                 order_id="pYtHoN!!!~~~~~~~~~~~~MB1234561672491601",  # a unique string
                 order_car=Car(),  # related car, car object class maybe
                 order_retailer=Retailer(),  # retailer object
                 order_creation_time=1672491601):  # UNIX time stamp
        """
        Parameters
        ----------
        order_id : str
            a string to store the order's id (default value is "pYtHoN!!!~~~~~~~~~~~~MB1234561672491601")
        order_car : Car object
            a car object (default value is Car())
        order_retailer : Retailer object
            a retailer object (default value is Retailer())
        order_creation_time : int
            an int to store the time of the creation of the order object (default value is 1672491601)
        """

        self.order_id = order_id
        self.order_car = order_car
        self.order_retailer = order_retailer
        self.order_creation_time = order_creation_time

    # create print function
    def __str__(self):
        """
        generate the order information as a formatted string

        Returns
        ----------
        str
            the order object information.
        """

        return ", ".join([
            str(self.order_id),
            str(self.order_car.car_code),
            str(self.order_retailer.retailer_id),
            str(self.order_creation_time)
        ])

    # function to generate the self.order_id
    def generate_order_id(self, car_code):
        """
        generate a random order id

        Returns
        ----------
        order_id : str
            a random order id.
        """

        # local variable
        str_1 = "~!@#$%^&*"

        # step 1
        # input the first string into the random_str
        random_str = random.choice(string.ascii_lowercase)
        # for looping 5 times to get 6 lowercase string
        for num_of_letter in range(5):
            # adding each new random lower case str to the random_str
            random_str += random.choice(string.ascii_lowercase)

        # step 2
        # create an empty variable to store the new random string
        new_random_str = ""
        # for looping the random_str to change each even letter to uppercase using enumerate function
        for alp_index, alph in enumerate(random_str):
            # if statement to check whether the index is even
            if (alp_index + 1) % 2 == 0:
                # if even then change it into lowercase letter then add to the new_random_str
                new_random_str += alph.upper()
            else:
                # if not, then directly add to the new_random_str
                new_random_str += alph

        # step 3
        # create an empty list to store the ASCII code of each letters
        list_ord = []
        # for looping the new_random_str to get the ASCII code
        for chara in new_random_str:
            # appending the ASCII code to the list_ord
            list_ord.append(ord(chara))

        # step_4
        # comprehension list to get the required step
        list_ord_remainder = [
            ((chara_ord ** 2) % len(str_1)) for chara_ord in list_ord
        ]

        # step 5
        # getting the list of chara according to the list_ord_remainder and str_1
        list_chara = [str_1[chara_ord] for chara_ord in list_ord_remainder]

        # step 6
        # for looping the list_chara to get a new string containing the special chara from str_1
        for chara_index, chara in enumerate(list_chara):
            # using the formula from step 6 then adding it into the new_random_str
            new_random_str = new_random_str + chara * chara_index

        # step 7
        # creating a new order_id
        order_id = new_random_str + car_code + str(self.order_creation_time)

        # change the self.order_id into the new order_id
        self.order_id = order_id

        # return order_id
        return order_id

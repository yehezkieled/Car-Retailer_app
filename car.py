# import libraries
import math


# create Car class
class Car:
    """
    A class used to represent a Car


    Attributes
    ----------
    car_code : str
        a string to store the car's code
    car_name : str
        a string to store the car's name
    car_capacity : int
        an int to store the car's capacity
    car_horsepower : int
        an int to store the car's horsepower
    car_weight : int
        an int to store the car's weight
    car_type : str
        a string to store the car's type

    Methods
    -------
    __str__()
        Return the car information as a formatted string
    probationary_licence_prohibited_vehicle()
        return boolean value if the car is a probationary licence prohibited vehicle
    found_matching_car()
        return boolean value if the car codes matches
    get_car_type()
        return the car type
    """
    # declaring the class attributes
    def __init__(self,
                 car_code="MB123456",
                 car_name="abcdefghij",
                 car_capacity=5,
                 car_horsepower=1000,
                 car_weight=200,
                 car_type="FWD"):
        """
        Parameters
        ----------
        car_code : str
            a string to store the car's code (default value is "MB123456")
        car_name : str
            a string to store the car's name (default value is "abcdefghij")
        car_capacity : int
            an int to store the car's capacity (default value is 5)
        car_horsepower : int
            an int to store the car's horsepower (default value is 1000)
        car_weight : int
            an int to store the car's weight (default value is 200)
        car_type : str
            a string to store the car's type (default value is "FWD")
        """

        self.car_code = car_code  # 2 upper(str) and 6 random digit
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower  # in kilowatts
        self.car_weight = car_weight  # in kilograms
        self.car_type = car_type  # should be either FWD, RWD, AWD

    # create print function
    def __str__(self):
        """
        generate the car information as a formatted string

        Returns
        ----------
        str
            the car object information.
        """

        # returning the joined sting of the car attributes
        return ", ".join([
            self.car_code,
            self.car_name,
            str(self.car_capacity),
            str(self.car_horsepower),
            str(self.car_weight),
            self.car_type
        ])

    # function to check whether a car is probationary prohibited or not
    def probationary_licence_prohibited_vehicle(self):
        """
        test whether the car is probationary licence prohibited vehicle or not

        Returns
        ----------
        bool
            True is probationary licence driver.
        """

        # calculation to check whether tha car is prohibited or not
        if math.ceil(int(self.car_horsepower) / int(self.car_weight)) * 1000 > 130:
            # return True probationary licence driver
            return True

        return False

    # function to check whether the car_code is the same as the self.car_code
    def found_matching_car(self, car_code):
        """
        test whether the car code matches

        Returns
        ----------
        bool
            True if it is matches.
        """

        # if statement to check whether the car_code is the same as the self.car_code
        if self.car_code == car_code:
            # return True if the same
            return True
        return False

    # function to return the car_type of the car object
    def get_car_type(self):
        """
        return the car type

        Returns
        ----------
        car_type : str
            the car type of the car object.
        """

        # return the car_type of the car object
        return self.car_type

# import libraries
import random


# create Retailer class
class Retailer:
    """
    A class used to represent an Order


    Attributes
    ----------
    retailer_id : str
        a string to store the retailer's id
    retailer_name : str
        a string to store the retailer's name

    Methods
    -------
    __str__()
        Return the retailer information as a formatted string
    generate_retailer_id()
        return a random retailer id
    """

    # declaring the class attributes
    def __init__(self,
                 retailer_id=12345678,
                 retailer_name="Halo"):
        """
        Parameters
        ----------
        retailer_id : str
            a string to store the retailer's id (default value is 12345678)
        retailer_name : str
            a string to store the retailer's name (default value is "Halo")
        """

        self.retailer_id = retailer_id  # must be unique 8 digit int
        self.retailer_name = retailer_name  # consists of letters andthe whitespace

    # create print function
    def __str__(self):
        """
        generate the retailer information as a formatted string

        Returns
        ----------
        str
            the retailer object information.
        """
        return str(self.retailer_id) + ", " + str(self.retailer_name)

    # function to create a new retailer id
    def generate_retailer_id(self, list_retailer):
        """
        generate a random retailer id

        Returns
        ----------
        none
        """

        # while function to check whether the new_id exists in the list_retailer
        while True:
            # create a new id
            new_id = random.randint(10000000, 99999999)
            # if the new_id is not inside the list_retailer then exit while loop
            if new_id not in list_retailer:
                break

        # change the self.retailer_id into the new_id
        self.retailer_id = new_id


#!/usr/bin/python3
""" Module 6-square: class Square """


class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()


# class Square():
#     """
#         Square: defines a square.
#         Attributes:
#             size (int): size of square.
#         Method:
#                 __init__ : init of size attribute for each instance.
#     """

#     def __init__(self, size=0, position=(0, 0)):

#         """ Initialization of attributes for instances
#             Args:
#                 size (int): size of the square.
#                 position (int tuple): position of the square
#         """
#         if not (isinstance(size, int)):
#             raise TypeError("size must be an integer")
#         if size < 0:
#             raise ValueError("size must be >= 0")

#         self.__size = size
#         self.__position = position

#     @property
#     def size(self):
#         """ getter function for private attribute size.
#             Returns:
#                 size.
#         """
#         return self.__size

#     @size.setter
#     def size(self, value):
#         """ setter function for private attribute size.
#             Args:
#                 value: size value to set to
#         """
#         if not (isinstance(value, int)):
#             raise TypeError("size must be an integer")
#         if value < 0:
#             raise ValueError("size must be >= 0")
#         self.__size = value

#     @property
#     def position(self):
#         """ getter function for private attribuet position
#             Returns:
#                 position.
#         """
#         return self.__position

#     @position.setter
#     def position(self, value):
#         """
#             setter function for private attribute position.
#             Args:
#                 value: position value to set to.
#         """
#         if isinstance(value, tuple) and len(value) == 2:
#             if isinstance(value[0], int) and isinstance(value[1], int):
#                 if value[0] >= 0 and value[1] >= 0:
#                     self.__position = value
#         else:
#             raise TypeError(
#               "position must be a tuple of 2 positive integers"
#             )

#     def area(self):
#         """
#              area of the square.
#         """
#         return self.__size * self.__size

#     def my_print(self):
#         """
#             prints the square with character #
#         """
#         if self.__size == 0:
#             print()
#         else:
#             i, j = 0, 0
#             temp = self.__position[0]
#             for i in range(self.__position[1]):
#                 print()
#             for j in range(self.__size):
#                 print("{}{}".format(" " * temp, "#" * self.__size))

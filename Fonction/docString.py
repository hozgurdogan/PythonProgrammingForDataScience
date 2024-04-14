#################
# Function Literacy
#################

# Printing a single letter
print("A")

# Printing two letters side by side
print("A", "B")

# Printing two letters with a custom separator
print("A", "B", sep="__")


##########################
# Creating Functions
##########################

def iki_ile_carp(girilen_sayi):
    """
    Multiplies the input number by two and returns it.

    Args:
        girilen_sayi (int, float): The number to be multiplied.

    Returns:
        int, float: The result of the multiplication.
    """
    return girilen_sayi * 2


def summer(girilen_sayi1, girilen_sayi2):
    """
    Sums two numbers and returns a string with the sum.

    Args:
        girilen_sayi1 (int, float): The first number for the sum operation.
        girilen_sayi2 (int, float): The second number for the sum operation.

    Returns:
        str: A message containing the sum of the input numbers.
    """
    sum_value = girilen_sayi1 + girilen_sayi2
    ekran_ciktisi = "The sum of the input numbers is " + str(sum_value)
    return ekran_ciktisi


# Getting a number from the user and performing multiplication
sayi1 = int(input("Please enter a number to multiply by 2: "))
print(iki_ile_carp(sayi1))

# Getting two numbers from the user to perform addition
sayi2 = int(input("Please enter another number for addition: "))
print(summer(sayi1, sayi2))

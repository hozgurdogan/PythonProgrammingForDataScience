def main_function(name, num1, num2):
    """
    Ana fonksiyon kişiyi selamlar ve yardımcı fonksiyonu verilen parametrelerle çağırır.

    Args:
        name (str): Selamlanacak kişinin ismi.
        num1 (int, float): Hesaplamada kullanılacak ilk sayı.
        num2 (int, float): Hesaplamada kullanılacak ikinci sayı.

    Returns:
        None.

    The main function greets a person and calls the helper function with given parameters.

    Args:
        name (str): The name of the person to be greeted.
        num1 (int, float): The first number to be used in the calculation.
        num2 (int, float): The second number to be used in the calculation.

    Returns:
        None.
    """
    # Kişiyi selamlayan mesajı yazdır (Prints a message greeting the person)
    print(f"Hello {name}, let's do some calculations with {num1} and {num2}.")

    # Yardımcı fonksiyonu verilen num1 ve num2 parametreleri ile çağır (Calls the helper function with num1 and num2 parameters)
    result = helper_function(num1, num2)

    # Yardımcı fonksiyondan gelen sonucu yazdır (Prints the result from the helper function)
    print(f"The result of the calculation is: {result}")

def helper_function(x, y):
    """
    İki sayı alır ve toplamlarını döndürür.

    Args:
        x (int, float): İlk sayı.
        y (int, float): İkinci sayı.

    Returns:
        int, float: İki sayının toplamı.

    Takes two numbers and returns their sum.

    Args:
        x (int, float): The first number.
        y (int, float): The second number.

    Returns:
        int, float: The sum of the two numbers.
    """
    # İki sayıyı topla ve sonucu döndür (Adds the two numbers and returns the result)
    return x + y

# Ana fonksiyonu parametrelerle birlikte çağırma (Calling the main function with parameters)
main_function("Alice", 10, 20)

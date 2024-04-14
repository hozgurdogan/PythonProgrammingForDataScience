def greet(name, message="Hello"):
    """
    Greets a person with a given message.

    Args:
        name (str): The name of the person to greet.
        message (str, optional): The greeting message to use. Default is "Hello".

    Returns:
        str: A greeting message.
    """
    return f"{message} {name}"

# Fonksiyonu sadece zorunlu argümanla çağırma (Calling the function with only the required argument)
print(greet("Alice"))

# Fonksiyonu her iki argümanla çağırma (Calling the function with both arguments)
print(greet("Bob", "Howdy"))

def calculate_area(width=10, height=5):
    """
    Calculates the area of a rectangle given width and height.
    If no values are provided, it uses default values of width 10 and height 5.

    Args:
        width (int, optional): The width of the rectangle. Default is 10.
        height (int, optional): The height of the rectangle. Default is 5.

    Returns:
        int: The area of the rectangle.
    """
    return width * height

# Fonksiyonu argüman vermeden çağırma (Calling the function without arguments)
print(f"Default area: {calculate_area()}")

# Fonksiyonu sadece bir argümanla çağırma (Calling the function with one argument)
print(f"Area with custom width: {calculate_area(width=20)}")

# Fonksiyonu her iki argümanla çağırma (Calling the function with both arguments)
print(f"Custom area: {calculate_area(width=20, height=10)}")

def make_coffee(size="medium", coffee_type="latte"):
    """
    Prepares a coffee with the given size and type.
    If no arguments are provided, it defaults to a medium latte.

    Args:
        size (str, optional): The size of the coffee. Default is "medium".
        coffee_type (str, optional): The type of coffee. Default is "latte".

    Returns:
        str: A description of the coffee being made.
    """
    return f"Making a {size} {coffee_type} coffee."

# Fonksiyonu ön tanımlı argümanlarla çağırma (Calling the function with default arguments)
print(make_coffee())

# Fonksiyonu farklı argümanlarla çağırma (Calling the function with different arguments)
print(make_coffee(size="large", coffee_type="espresso"))

# Daha fazla örnekle devam etmek (Continuing with more examples)
# Buradan sonrasını sizin belirlediğiniz başka fonksiyonlar ve kullanım örnekleriyle doldurabilirsiniz.
# Örneğin, bir kullanıcı kayıt fonksiyonu yazabilir ve kullanıcı adı için bir ön tanımlı değer atayabilirsiniz.

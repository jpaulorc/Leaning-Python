""" Assertions

    An assert statement checks whether a condition is true. 
    If a condition evaluates to True, a program will keep running. 
    If a condition is false, the program will return an AssertionError.

    assert condition, message

    condition (required): the condition for which you want to test
    message (optional): the message you want to display upon execution of the assert statement

    Why not just use an if-statement?
    The goal of using assertions is to let developers find the likely root cause of a bug morequickly.
    You can see how the exception points out the exact line of code containing the failed assertion.

    Problem:
    The biggest problem with using asserts in Python is that assertions can be globally disabled, 
    so never use assertions to do data validation.
"""
def apply_discount(product, discount):
    price = float(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], "Discount amount not allowed."
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900}

print(f"Original Price: {shoes['price']}")
print(f"Price with 25% discount: {apply_discount(shoes, 0.25)}")
print(f"Price with 200% discount: {apply_discount(shoes, 2.0)}")
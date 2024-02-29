import random
from typing import List


def generate_random_integers(lower: int, upper: int, length: int) -> List[int]:
    """Generate a list of random integers within a specified range.

    :param lower: The lower bound of the range.
    :param upper: The upper bound of the range.
    :param length: The length of the list to generate.
    :return: A list of random integers.
    """
    return [random.randint(lower, upper) for _ in range(length)]


def count_hungry_customers(
    cookie_stack: List[int], customer_queue: List[int]
) -> int:
    """Count the number of hungry customers based on the cookie stack and
    customer queue.

    :param cookie_stack: List representing the stack of cookies.
    :param customer_queue: List representing the queue of customers.
    :return: The number of customers who couldn't get a cookie.
    """
    # One-to-one correspondence between cookie_stack and customer_queue will
    # result in 0 hungry customers.
    if cookie_stack == customer_queue:
        return 0

    # Initialize the count of each type of customer to 0
    # (It has to be taken from the set of the elements in cookie_stack PLUS
    # customer_queue because set(cookie_stack) may not necessarily equal
    # set(customer_queue). This is done to avoid a KeyError when accessing
    # customer_frequency.)
    customer_frequency = {c: 0 for c in set(cookie_stack + customer_queue)}

    # Obtain the count of each type of customer
    for c in customer_queue:
        customer_frequency[c] += 1

    # Reduce the number of hungry customers based on the cookie that is on top
    # of the stack
    # (If there are no customers that can eat the cookie on the top of the
    # stack, then the current customer onwards will go hungry.)
    for c in cookie_stack:
        if customer_frequency[c]:
            customer_frequency[c] -= 1
        else:
            break

    # Return the total number of hungry customers
    return sum(customer_frequency.values())


def main() -> None:
    """Main function."""
    lower, upper, length = 0, 1, 10
    cookie_stack = generate_random_integers(lower, upper, length)
    customer_queue = generate_random_integers(lower, upper, length)

    print(f"Cookie Stack: {cookie_stack}")
    print(f"Customer Queue: {customer_queue}")

    hungry_customers = count_hungry_customers(cookie_stack, customer_queue)
    print(f"\nNumber of Hungry Customers: {hungry_customers}")


if __name__ == "__main__":
    main()

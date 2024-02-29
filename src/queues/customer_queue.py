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
    # Create a set of all distinct POSSIBLE customers
    all_customers = set(cookie_stack + customer_queue)

    # Initialize a dictionary to store the count of each customer
    customer_frequency = {c: 0 for c in all_customers}

    # Count the occurrences of each customer in the queue
    for customer in customer_queue:
        customer_frequency[customer] += 1

    # Reduce the count of customers based on the cookies available in the stack
    for cookie in cookie_stack:
        if customer_frequency.get(cookie, 0) > 0:
            customer_frequency[cookie] -= 1
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

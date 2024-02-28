import random
from typing import List


def generate_random_numbers(lower: int, upper: int, length: int) -> List[int]:
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
    """Count the number of hungry customers based on cookie stack and customer
    queue.

    :param cookie_stack: List representing the stack of available cookies.
    :param customer_queue: List representing the queue of hungry customers.
    :return: The number of customers who couldn't get a cookie.
    """
    if cookie_stack == customer_queue:
        return 0

    customer_frequency = {c: 0 for c in set(customer_queue)}

    for c in customer_queue:
        customer_frequency[c] += 1

    for c in cookie_stack:
        if customer_frequency[c]:
            customer_frequency[c] -= 1
        else:
            break

    return sum(customer_frequency.values())


def main() -> None:
    """Main function."""
    lower, upper, length = 0, 1, 10
    cookie_stack = generate_random_numbers(lower, upper, length)
    customer_queue = generate_random_numbers(lower, upper, length)

    print(f"Cookie Stack: {cookie_stack}")
    print(f"Customer Queue: {customer_queue}")

    hungry_customers = count_hungry_customers(cookie_stack, customer_queue)
    print(f"\nNumber of Hungry Customers: {hungry_customers}")


if __name__ == "__main__":
    main()

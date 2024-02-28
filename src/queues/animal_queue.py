from collections import deque
import random
from typing import List


class AnimalQueue:
    """A queue implemented for animal adoption, supporting dequeue operations
    for cats and dogs.
    """

    def __init__(self) -> None:
        """Initialize an empty queue."""
        self.queue: deque[str] = deque()

    def __str__(self) -> str:
        """Return a string representation of the queue.

        :return: String representation of the queue.
        """
        if self.is_empty():
            return "The queue is empty!"
        else:
            queue_str = ', '.join(self.queue)
            return f"Front -> {queue_str} <- Back"

    def enqueue(self, animal: str) -> None:
        """Add an animal to the back of the queue.

        :param animal: The animal to enqueue.
        """
        self.queue.append(animal)

    def dequeue(self) -> str:
        """Remove and return the front animal from the queue.

        :return: The dequeued animal.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("The queue is empty!")

        return self.queue.popleft()

    def dequeue_cat(self) -> str:
        """Remove and return the first cat from the queue.

        :return: The dequeued cat.
        :raises IndexError: If the queue is empty or there are no cats in the
                            queue.
        """
        if self.is_empty():
            raise IndexError("The queue is empty!")

        try:
            self.queue.remove("Cat")
        except ValueError:
            raise IndexError("There are no cats in the queue!")

        return "Cat"

    def dequeue_dog(self) -> str:
        """Remove and return the first dog from the queue.

        :return: The dequeued dog.
        :raises IndexError: If the queue is empty or there are no dogs in the
                            queue.
        """
        if self.is_empty():
            raise IndexError("The queue is empty!")

        try:
            self.queue.remove("Dog")
        except ValueError:
            raise IndexError("There are no dogs in the queue!")

        return "Dog"

    def peek(self) -> str:
        """Return the front animal of the queue without removing it.

        :return: The front animal of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("The queue is empty!")

        return self.queue[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return not self.queue

    def display_queue(self) -> None:
        """Display the contents of the queue."""
        print(f"{self}")
        print(f"Is the queue empty? {'Yes' if self.is_empty() else 'No'}")
        if not self.is_empty():
            print(f"The front animal of the queue is {self.peek()}.")


def generate_random_animals(length: int) -> List[str]:
    """Generate a random list of animal types (Cat or Dog).

    :param length: The length of the list to generate.
    :return: A list of random animal types.
    """
    return ["Cat" if random.random() < 0.5 else "Dog" for _ in range(length)]


def main() -> None:
    """Main function."""
    random_animals = generate_random_animals(15)
    animal_queue = AnimalQueue()

    print("Before Enqueueing Animals in the Queue")
    animal_queue.display_queue()

    for animal in random_animals:
        animal_queue.enqueue(animal)
    print("\nAfter Enqueueing Animals in the Queue")
    animal_queue.display_queue()

    try:
        dequeued_cat = animal_queue.dequeue_cat()
        print("\nAfter Dequeueing the First Cat from the Queue")
        animal_queue.display_queue()
        print(f"The animal dequeued from the queue is {dequeued_cat}.")

        dequeued_dog = animal_queue.dequeue_dog()
        print("\nAfter Dequeueing the First Dog from the Queue")
        animal_queue.display_queue()
        print(f"The animal dequeued from the queue is {dequeued_dog}.")

        dequeued_animal = animal_queue.dequeue()
        print("\nAfter Dequeueing the Front Animal from the Queue")
        animal_queue.display_queue()
        print(f"The animal dequeued from the queue is {dequeued_animal}.")
    except IndexError as e:
        print(f'Error: "{e}".')

    while not animal_queue.is_empty():
        animal_queue.dequeue()
    print("\nAfter Dequeueing the Rest of the Animals from the Queue")
    animal_queue.display_queue()


if __name__ == "__main__":
    main()

# Function becomes a generator by including yield
# calling a generator functoin returns an object that implements __iter__() and __next__()
# code inside only runs when iteration begins, in a for loop or via next()
# when function ends, StopIteration raised automatically
# generators keep their local variables alive between yields
# generator functions return an iterator immediately, use generators for producing sequences lazily, functions for compute and return complete result

def count_up_to(limit):
    """Generates numbers from 1 up to (and including) the limit.

    Args:
        limit (int): The upper limit for counting.
    """
    print("Generator function started...")
    n = 1

    while n <= limit:
        print(f"Yielding {n}")
        yield n
        print(f"Resumed after yielding {n}.")
        n += 1

    print("Generator function finished.")

count_gen = count_up_to(3);
print(f"Returned object: {count_gen} of type {type(count_gen)}")

for number in count_gen:
    print(number)

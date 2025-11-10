from itertools import chain
from itertools import islice
from itertools import (
        groupby, zip_longest, accumulate, product, permutations, combinations,
        filterfalse, dropwhile, takewhile, cycle, count, repeat
    )

user_data=["aniket","Ravi"]
System_data=["Server1","Server2"]


for i in chain(user_data,System_data):
    print(i)
    

data_stream = range(100000)
page_size = 10

def get_page(stream, page_number):
    start = (page_number - 1) * page_size
    end = start + page_size
    return list(islice(stream, start, end))


for page_num in range(1, 4):
    page_data = get_page(data_stream, page_num)
    print(f"Page {page_num} data:", page_data)
    print(f"Items {(page_num-1)*page_size + 1} to {page_num*page_size}")
    

    names = ["bob", "barbara", "alice", "ann", "bryan"]
    for key, group in groupby(sorted(names), key=lambda s: s[0]):
        print("group", key, "->", list(group))

    print("zip_longest:", list(zip_longest([1, 2, 3], ["a", "b"], fillvalue=None)))

    print("accumulate (sum):", list(accumulate([1, 2, 3, 4])))
    print("accumulate (running max):", list(accumulate([1, 3, 2, 5], func=max)))

    print("product:", list(product([0, 1], repeat=2)))

    print("permutations (len2):", list(permutations([1, 2, 3], 2)))

    print("combinations (len2):", list(combinations([1, 2, 3], 2)))

    print("filterfalse (keep odds):", list(filterfalse(lambda x: x % 2 == 1, [1, 2, 3, 4])))

    nums = [0, 1, 2, 3, 0, 4]
    print("dropwhile <3:", list(dropwhile(lambda x: x < 3, nums)))  
    print("takewhile <3:", list(takewhile(lambda x: x < 3, nums)))   

    c = cycle("AB")
    print("cycle first 6:", [next(c) for _ in range(6)])

    ctr = count(10, 2)
    print("count with items:", [next(ctr) for _ in range(3)]) 

    print("repeat 3 times:", list(repeat("X", 3)))
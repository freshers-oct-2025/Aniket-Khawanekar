
nums = [1, 2, 3, 4, 5]

it=iter(nums)
print(next(it))  
print(next(it))    
print(it.__next__())      

# for n in it:
#     print(n)
    

class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()
for i in values:
    print(i)


# def demo_list_iterator():
#     data = ['a', 'b', 'c']
#     it = iter(data)
#     print("Example 1: list iterator using next():")
#     try:
#         while True:
#             item = next(it)
#             print(item, end=' ')
#     except StopIteration:
#         print("\n-- iterator exhausted --")
#     print()



# class Countdown:
#     def __init__(self, start):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current <= 0:
#             raise StopIteration
#         value = self.current
#         self.current -= 1
#         return value


# def demo_countdown():
#     print("Example 2: custom iterator (Countdown):")
#     for n in Countdown(5):
#         print(n, end=' ')
#     print("\n")





# if __name__ == "__main__":
#     demo_list_iterator()
#     demo_countdown()


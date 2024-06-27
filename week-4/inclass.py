names = ["Ricky", "Michael", "John", "Robert"]
for word in names:
    if "R" in word:
        print(word)

print(list(range(1, 5)))


numbers = [2, 3, 4, 5]
i = 0

while i < len(numbers):
    numbers[i] = numbers[i] ** 2
    i += 1
print(numbers)


numbers.sort(reverse=True)
print(numbers)

numbers = numbers.sort()
print(numbers)


mock_data = {
    "Apple": 0.50,
    "Banana": 0.20,
    "Mango": 0.99,
    "Coconut": 2.99,
    "Pineapple": 3.99,
}
def middle_number(numbers):
    return sorted(numbers, reverse=True)[(len(numbers) + 1) // 2 - 1]


input_numbers = int(input())
result = middle_number(input_numbers)
print(result)

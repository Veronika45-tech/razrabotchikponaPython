numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
filtered_num = [num for num in numbers if num is not None]

sum_num = sum(filtered_num)
count_num = len(numbers)

average = sum_num / count_num

numbers = [average if num is None else num for num in numbers]
print("Измененный список:", numbers)
def convert_to_bin(n):
    return bin(n)


def count_one_in_bits(n):
    count = 0
    count_index = 0
    converted = str(convert_to_bin(n))
    for i in converted:
        if converted[count_index] == '1':
            count += 1
        count_index += 1
    return count


num = 9876
print(f"Bin: {convert_to_bin(num)}")
print(f'1 in {convert_to_bin(num)} = {count_one_in_bits(num)}')

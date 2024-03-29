def find_max_position(lst):
    return [i for i, val in enumerate(lst) if val == max(lst)] if lst else None

# Sử dụng hàm và nhập vào list số nguyên
nums = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split(',')))
max_positions = find_max_position(nums)
print(f"Giá trị lớn nhất là {nums[max_positions[0]]} ở vị trí {max_positions}" if max_positions else "Danh sách trống")


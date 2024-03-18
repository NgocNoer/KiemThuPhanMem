from aifc import Error
from main import calculate_discount

# Kiểm thử giá trị biên
test_cases_boundary_value = [
    # Loại A - Nhóm 0: Giá trị = 99
    {
        'item_type': 'A',
        'total_amount': 99,
        'expected_output': Error
    },
    # Loại A - Nhóm 1: Giá trị = 100
    {
        'item_type': 'A',
        'total_amount': 100,
        'expected_output': 0
    },
    # Loại A - Nhóm 2: Giá trị = 101
    {
        'item_type': 'A',
        'total_amount': 101,
        'expected_output': 0
    },
    # Loại A - Nhóm 3: Giá trị = 500,000
    {
        'item_type': 'A',
        'total_amount': 500000,
        'expected_output': 0.05 * 500000
    },
    # Loại A - Nhóm 4: Giá trị = 999,999
    {
        'item_type': 'A',
        'total_amount': 999999,
        'expected_output': 0.1 * 999999
    },
    # Loại A - Nhóm 5: Giá trị = 1,000,000
    {
        'item_type': 'A',
        'total_amount': 1000000,
        'expected_output': 0.1 * 1000000
    },
    # Loại A - Nhóm 6: Giá trị = 1,000,001
    {
        'item_type': 'A',
        'total_amount': 1000001,
        'expected_output': 0.15 * 1000001
    },
    
    # Loại B - Nhóm 0: Giá trị = 99
    {
        'item_type': 'B',
        'total_amount': 99,
        'expected_output': Error
    },
    # Loại B - Nhóm 1: Giá trị = 100
    {
        'item_type': 'B',
        'total_amount': 100,
        'expected_output': 0
    },
    # Loại B - Nhóm 2: Giá trị = 101
    {
        'item_type': 'B',
        'total_amount': 101,
        'expected_output': 0
    },
    # Loại B - Nhóm 3: Giá trị = 500,000
    {
        'item_type': 'B',
        'total_amount': 500000,
        'expected_output': 0.07 * 500000
    },
    # Loại B - Nhóm 4: Giá trị = 999,999
    {
        'item_type': 'B',
        'total_amount': 999999,
        'expected_output': 0.12 * 999999
    },
    # Loại B - Nhóm 5: Giá trị = 1,000,000
    {
        'item_type': 'B',
        'total_amount': 1000000,
        'expected_output': 0.12 * 1000000
    },
    # Loại B - Nhóm 6: Giá trị = 1,000,001
    {
        'item_type': 'B',
        'total_amount': 1000001,
        'expected_output': 0.18 * 1000001
    },
]


for test_case in test_cases_boundary_value:
    item_type = test_case['item_type']
    total_amount = test_case['total_amount']
    expected_output = test_case['expected_output']
    
    try:
        actual_output = calculate_discount(total_amount, item_type)
        assert actual_output == expected_output
        print(f"Test case passed: Item_Type={item_type}, Total_Amount={total_amount}, Expected_Output={expected_output}, Actual_Output={actual_output}")
    except Exception as e:
        print(f"Test case failed: Item_Type={item_type}, Total_Amount={total_amount}, Expected_Output={expected_output}, Error={str(e)}")

from aifc import Error
from main import calculate_discount

# Kiểm thử theo dòng điều khiển
test_cases_control_line = [
    # Loại A - Nhóm 0: Giá trị < 100
    {
        'item_type': 'A',
        'total_amount': 20,
        'expected_output': Error
    },
    # Loại A - Nhóm 1: Giá trị <= 100,000
    {
        'item_type': 'A',
        'total_amount': 50000,
        'expected_output': 0
    },
    # Loại A - Nhóm 2: 100,001 <= Giá trị <= 500,000
    {
        'item_type': 'A',
        'total_amount': 250000,
        'expected_output': 0.05 * 250000
    },
    # Loại A - Nhóm 3: 500,001 <= Giá trị <= 1,000,000
    {
        'item_type': 'A',
        'total_amount': 750000,
        'expected_output': 0.1 * 750000
    },
    # Loại A - Nhóm 4: Giá trị >= 1,000,001
    {
        'item_type': 'A',
        'total_amount': 1500000,
        'expected_output': 0.15 * 1500000
    },

    # Loại B - Nhóm 0: Giá trị < 100
    {
        'item_type': 'A',
        'total_amount': 20,
        'expected_output': Error
    },
    # Loại B - Nhóm 1: Giá trị <= 100,000
    {
        'item_type': 'B',
        'total_amount': 50000,
        'expected_output': 0
    },
    # Loại B - Nhóm 2: 100,001 <= Giá trị <= 500,000
    {
        'item_type': 'B',
        'total_amount': 500000,
        'expected_output': 0.07 * 500000
    },
    # Loại B - Nhóm 3: 500,001 <= Giá trị <= 1,000,000
    {
        'item_type': 'B',
        'total_amount': 1000000,
        'expected_output': 0.12 * 1000000
    },
    # Loại B - Nhóm 4: Giá trị >= 1,000,001
    {
        'item_type': 'B',
        'total_amount': 2000000,
       'expected_output': 0.18 * 2000000
    }
]


for test_case in test_cases_control_line:
    item_type = test_case['item_type']
    total_amount = test_case['total_amount']
    expected_output = test_case['expected_output']
    
    try:
        actual_output = calculate_discount(total_amount, item_type)
        assert actual_output == expected_output
        print(f"Test case passed: Item_Type={item_type}, Total_Amount={total_amount}, Expected_Output={expected_output}, Actual_Output={actual_output}")
    except Exception as e:
        print(f"Test case failed: Item_Type={item_type}, Total_Amount={total_amount}, Expected_Output={expected_output}, Error={str(e)}")
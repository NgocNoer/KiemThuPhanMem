from main import calculate_discount
from aifc import Error

# Kiểm thử bảng quyết định
test_cases_decision_table = [
    {"Item_Type": "A", "Total_Amount": 20, "Expected_Output": Error},
    {"Item_Type": "A", "Total_Amount": 50000, "Expected_Output": 0},
    {"Item_Type": "A", "Total_Amount": 250000, "Expected_Output": 0.05 * 250000},
    {"Item_Type": "A", "Total_Amount": 750000, "Expected_Output": 0.1 * 750000},
    {"Item_Type": "A", "Total_Amount": 1500000, "Expected_Output": 0.15 * 1500000},

    {"Item_Type": "B", "Total_Amount": 20, "Expected_Output": Error},
    {"Item_Type": "B", "Total_Amount": 50000, "Expected_Output": 0},
    {"Item_Type": "B", "Total_Amount": 500000, "Expected_Output": 0.07 * 500000},
    {"Item_Type": "B", "Total_Amount": 1000000, "Expected_Output": 0.12 * 1000000},
    {"Item_Type": "B", "Total_Amount": 2000000, "Expected_Output": 0.18 * 2000000},
]

for test_case in test_cases_decision_table:
    item_type = test_case['Item_Type']
    total_amount = test_case['Total_Amount']
    expected_output = test_case['Expected_Output']

    try:
        actual_output = calculate_discount(total_amount, item_type)
        assert actual_output == expected_output
        print(f"Test case passed: Item_Type={item_type}, Total_Amount={total_amount}, Expected_Output={expected_output}, Actual_Output={actual_output}")
    except Exception as e:
        print(f"Test case failed: Item_Type={item_type}, Total_Amount={total_amount}, Expected_Output={expected_output}, Error={str(e)}")
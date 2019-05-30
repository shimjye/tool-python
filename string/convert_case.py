#-*- coding: utf-8 -*-

def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0].lower() + ''.join(x.title() for x in components[1:])


# main
if __name__ == "__main__":
    print(to_camel_case('test_case_number1')) #testCaseNumber1
    print(to_camel_case('TEST_CASE_NUMBER2')) #testCaseNumber2
    print(to_camel_case('test_CASE_number3')) #testCaseNumber3


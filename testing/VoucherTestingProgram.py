import filecmp
from FileHandler import FileHandler
from VoucherTestClass import VoucherTests
def main():
    testobj = VoucherTests()
    print("Start of Testing Program!")
    print("--------------------------------")
    print("~~~~~~~~~~~~~Test 1~~~~~~~~~~~~~")
    print("Test 1: Handling syntax/structure of header errors.")
    print("Expected error output:\nError! Incorrect Header structure.")
    print("Program output:")
    result1 = testobj.headerSyntaxTest()
    if result1:
        print("Test 1 Result: Passed!")
    else:
        print("Test 1 Result: Failed!")    
    print("--------------------------------")
    
    
    
    print("~~~~~~~~~~~~~Test 2~~~~~~~~~~~~~")
    print("Test 2: Header Dictionary Data Saving.")
    result2 = testobj.headerDataTest()
    if result2:
        print("Test 2 Result: Passed!")
    else:
        print("Test 2 Result: Failed!")
    print("--------------------------------")    
    
    
    print("~~~~~~~~~~~~~Test 3~~~~~~~~~~~~~")
    print("Test 3: Data Validation Testing should produce error for 2 of the vouchers.")
    result3 = testobj.fileValidationTest()
    if result3:
        print("Test 3 Result: Passed!")
    else:
        print("Test 3 Result: Failed!")    
    print("--------------------------------")   
    
    print("~~~~~~~~~~~~~Test 4~~~~~~~~~~~~~")
    print("Test 4: File output test to ensure structure of output file matches expected file.")
    result4 = testobj.fileOutputTest()
    if result4:
        print("Test 4 Result: Passed!")
    else:
        print("Test 4 Result: Failed!")    
    print("--------------------------------")            
    print("~~~~~~~~~Tests Summary~~~~~~~~~~")
    if result1:
        print("Test 1 Result: Passed!")
    else:
        print("Test 1 Result: Failed!")
    if result2:
        print("Test 2 Result: Passed!")
    else:
        print("Test 2 Result: Failed!")
    if result3:
        print("Test 3 Result: Passed!")
    else:
        print("Test 3 Result: Failed!")
    if result4:
        print("Test 4 Result: Passed!")
    else:
        print("Test 4 Result: Failed!")
    print("--------------------------------")
    print("End of Testing Program!")

if __name__ == '__main__':
    main()


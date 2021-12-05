import filecmp
from FileHandler import FileHandler
from VoucherTestClass import VoucherTests
def main():
    testobj = VoucherTests()
    print("Start of Testing Program!")
    #print(filecmp.cmp('demo_result.txt', 'expected.txt'))
    print("Testing program functions...")
    testobj.functionTests()
    

    

if __name__ == '__main__':
    main()


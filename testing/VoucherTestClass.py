import filecmp
from FileHandler import FileHandler
class VoucherTests(object):
    
    def __init__(self):
        pass
    def headerSyntaxTest(self): #Tests error handling when given a file with incorrect header structure/syntax
        voucherObj = FileHandler("headerSyntaxTest")
        
        result = voucherObj.checkHeaderSyntax()
        if result == False:
            return True
        else:
            return False        
    def headerDataTest(self): #Tests to see that the data was saved from the header into the dictionary correctly.
        voucherObj = FileHandler("headerDictionaryTest")
        expected_header_dict = {'download_datetime': '2015-11-06 1357', 'order_datetime': '2015-11-05 1014', 'layout_name': 'Demo', 'columns': '6', 'column_width': '25', 'column_spacing': '5', 'left_margin': '0', 'row_spacing': '5', 'line_item1': 'pin', 'line_item2': 'empty', 'line_item3': 'empty', 'line_item4': 'description', 'line_item5': 'serial_number', 'line_item6': 'expiry_date', 'voucher_summary1': 'Cell-C 10.00,10,100.00', 'voucher_summary2': 'MTN 5.00,5,25.00', 'voucher_summary3': 'Vodacom 12.00,5,60.00', 'voucher_fields': 'description,pin,serial_number,expiry_date'}
        generated_header_dict = voucherObj.getHeaderDict()
        if expected_header_dict == generated_header_dict:
            return True
        else:
            return False
    def fileValidationTest(self): #Tests the error handling when the voucher amount stated in  the header does not match the count in the data( fileValidationTest.txt contains 2 mistakes which should cause file validation errors).
        voucherObj = FileHandler("fileValidationTest")
        result = voucherObj.validateData()
        if result == False:
            return True
        else:
            return False
    def fileOutputTest(self): #Does a byte by byte test on the contents of the files to ensure they are matching the structure exactly.
        voucherObj = FileHandler("fileOutputTestInput")
        voucherObj.format()
        
        result = filecmp.cmp('fileOutputTestInput_result.txt', 'fileOutputTestExpected.txt')
        if result == True:
            return True
        else:
            return False        
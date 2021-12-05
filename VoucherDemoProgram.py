import sys
def main():
    from FileHandler import FileHandler
    
    print("Please enter the file name(without the .txt extension):")
    try:
        voucherObj = FileHandler(input())
        voucherObj.format()
        
    except:
        print("File not found or incorrect file name.")
        quit()

if __name__ == '__main__':
    main()

    

import sys
def main():
    from FileHandler import FileHandler
    
    print("Please enter the file name(without the .txt extension):")
    try:
        voucherObj = FileHandler(input())
        
    except:
        print("File not found or incorrect file name.")
        quit()
 
        
    
    #data = voucherObj.getData()
    #print(data)
if __name__ == '__main__':
    main()

    

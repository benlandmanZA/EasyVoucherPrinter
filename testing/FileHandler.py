import numpy as np
import math
class FileHandler(object):
   
    
    def __init__(self, file_name):
        
        self.file_name = file_name
        self.header_dictionary = {"download_datetime":"","order_datetime": "","layout_name":"","columns":0,"column_width":0,"column_spacing":0,"left_margin":0,"row_spacing":5,"line_item1":"","line_item2":"","line_item3":"","line_item4":"","line_item5":"","line_item6":"","voucher_summary1":"","voucher_summary2":"","voucher_summary3":"","voucher_fields":""}
        with open(self.file_name+".txt", 'r') as input_file:
            all_data = [line.strip() for line in input_file.readlines()]
            self.header_data = all_data[:18]
            self.data = all_data[18:]
            if self.checkHeaderSyntax() == False:
                print("Error! Incorrect Header format.")
            else:
                self.populateHeaderDictionary()
                if self.validateData() == True:
                    print("Data Validation Success! Formatting...")
                    self.format()
                
                
            
    def checkHeaderSyntax(self):
        header_syntax = ["download_datetime","order_datetime","layout_name","columns","column_width","column_spacing","left_margin","row_spacing","line_item","line_item","line_item","line_item","line_item","line_item","voucher_summary","voucher_summary","voucher_summary","voucher_fields"]
        i = 0
        for item in header_syntax:
            
            header_item_raw = self.header_data[i]
            header_item_name = header_item_raw.split(":")[0]
            if item == header_item_name:
               
                i+=1
            else:
                return False
                
        return True   
    def populateHeaderDictionary(self):
        i = 0
        for item in self.header_dictionary:
           
            header_item_raw = self.header_data[i]
            header_item_value = header_item_raw.split(":")[1]
           # print("value:",header_item_value)
            
            self.header_dictionary[item] = header_item_value
            #print("dictionary:",self.header_dictionary[item])
            i+=1
    
    def validateData(self):
        success = False
        summary1success = False
        summary2success = False
        summary3success = False
        summary_dict = {}
        failed_list = []
        summary1Key = self.header_dictionary["voucher_summary1"].split(",")[0]
        summary2Key = self.header_dictionary["voucher_summary2"].split(",")[0]
        summary3Key = self.header_dictionary["voucher_summary3"].split(",")[0]
        
        summary1Amount = int(self.header_dictionary["voucher_summary1"].split(",")[1])
        summary2Amount = int(self.header_dictionary["voucher_summary2"].split(",")[1])
        summary3Amount = int(self.header_dictionary["voucher_summary3"].split(",")[1])        
        
        summary_dict[summary1Key] = summary1Amount
        summary_dict[summary2Key] = summary2Amount
        summary_dict[summary3Key] = summary3Amount
        
        summary1Count = 0
        summary2Count = 0
        summary3Count = 0
        for voucher in self.data:
            if voucher.split(",")[0] in summary_dict:
                if voucher.split(",")[0] == summary1Key:
                    summary1Count+=1
                elif voucher.split(",")[0] == summary2Key:
                    summary2Count+=1
                elif voucher.split(",")[0] == summary3Key:
                    summary3Count+=1
                
            else:
                success = False
                
               
        if summary1Count == summary1Amount:
            
            summary1success = True
            
        else:
            failed_list.append([summary1Key, summary1Amount, summary1Count])
            
        
        if summary2Count == summary2Amount:
            summary2success = True
        else:
            failed_list.append([summary2Key, summary2Amount, summary2Count])       
        
        
        if summary3Count == summary3Amount:
            summary3success = True
        else:
            failed_list.append([summary3Key, summary3Amount, summary3Count])         
        
        
        if summary1success and summary2success and summary3success:
            success = True
        if success:
            return True
        else:
            print("Error! Data Validation failed with the following Voucher(s):")
            for item in failed_list:
                print("Voucher summary name:",item[0])
                print("Voucher amount stated in header:",item[1])
                print("Voucher amount found in data:",item[2])
                print("------------------------------------")
            return False
        
    
    def format(self):
        with open(self.file_name+"_result.txt", 'w+') as export_file:
            print("formatted")
            #print(self.data)
        
            sorted_array = []
            count = 0
            for z in self.data:
                
                temp_item = ["",""]
                temp_item.insert(0, z.split(",")[1])
                temp_item.insert(3, z.split(",")[0])
                temp_item.insert(4, z.split(",")[2])
                temp_item.insert(5, z.split(",")[3])
                
                sorted_array.insert(count,temp_item)
                
                count+=1
            
            columns = int(self.header_dictionary["columns"])
            mover = 0
            column_spacing = int(self.header_dictionary["column_spacing"])
            column_width = int(self.header_dictionary["column_width"])
            row_spacing = int(self.header_dictionary["row_spacing"])
            total_width = column_spacing+column_width+1
            total_rows = math.ceil(len(sorted_array)/columns)
            columnStr = "{:<"+str(total_width)+"}" 
            for k in range(total_rows):
                for x in range(6):
                    for y in range(0+mover,columns+mover):
                        
                        try:
                            write = columnStr.format(sorted_array[y][x])
                            export_file.write(write)
                        except:
                            pass
                        finally:
                            pass
                            
                    export_file.write("\n")
                mover+=columns
                export_file.write("\n"*row_spacing)  
            
    def index_in_list(self, a_list, index):
        return index < len(a_list)    
    def getData(self):
        return self.data
    def getHeaderData(self):
        return self.header_data
    def getHeaderDict(self):
        return self.header_dictionary
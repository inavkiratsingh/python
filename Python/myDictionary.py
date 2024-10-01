navDict = {"DOB":"10-3-2004" ,
           "Class":"12th" ,
           "Stream":"Non-medical" ,
           "Dream":"Engineer"}
# print(type(navDict))
print("Enter what you want to know from following")
print("DOB")
print("Class")
print("Stream")
print("Dream")

key = input("ENTER HERE  -", )
value = navDict[key]
print(key, " :-" , value)
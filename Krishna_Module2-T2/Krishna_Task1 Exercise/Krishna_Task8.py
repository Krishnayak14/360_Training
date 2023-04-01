#If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?

a= "To check string is working fine"
a= True
print(a)
#Reason: It will change its value and will give result for updated line or last modified value because
# the original value stored in 'a' will be overwritten by the new value. The new value will occupy the memory
#location that was previously used to store the original value.

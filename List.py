#List are mutable and ordered  with square brackets
#Supports nesting by adding other lists in a list

List1 = [1, 4.0,"Disco",[1,3.5,"John"],6, "Alone"]

## List slicing with the last index larger tham the last index you want
List1[1:3] #Outputs 4.0 and Disco

#Method extend adds elements to the list
List1.extend([3, "Kiragu"])

#Method split separates the elemts

List2 ="List2 split".split()

#Method append adds one element to the list

List3 = [1,5]

List3.append([3.4])
List3
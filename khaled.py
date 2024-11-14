
def northwest_method_fun(list_of_rows,rows,columns,demand_list,supply_list):
    sum=0
    i=0
    j=0
    check = True
    while check:
        if demand_list[0] > supply_list[0]:
            list_of_rows[i][j]["value"]=supply_list[0]
            sum += list_of_rows[i][j]["value"] * list_of_rows[i][j]["cells"]
            demand_list[0] -=supply_list[0]
            supply_list.pop(0)
            i +=1 # this is numver of rows incremented by 1
        elif demand_list[0] == supply_list[0]:
            list_of_rows[i][j]["value"]=supply_list[0]
            sum += list_of_rows[i][j]["value"] * list_of_rows[i][j]["cells"]
            supply_list.pop(0)
            demand_list.pop(0)
            i +=1 # this is numver of rows incremented by 1
            j +=1
        else:
            list_of_rows[i][j]["value"]=demand_list[0]
            sum += list_of_rows[i][j]["value"] * list_of_rows[i][j]["cells"]
            supply_list[0] -=demand_list[0]
            demand_list.pop(0)
            j +=1
        if demand_list.__len__() == 0 or supply_list.__len__() == 0:
            check = False
           
    # print(list_of_rows)
    print("Total cost: ", sum)






list_of_rows =[]

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
supply_list = []
demand_list = []

print("Enter the matrix elements row by row:")
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element at position [{i+1}, {j+1}]: "))
        row.append({"cells":element,"value":None})
    list_of_rows.append(row)
    
for i in range(rows):
    inner=int(input(f"Enter the number of supply from top to down : "))
    supply_list.append(inner)
for i in range (columns):
    inner=int(input(f"Enter the number of demand from left to right "))
    demand_list.append(inner)
    

                
                
            
northwest_method_fun(list_of_rows,rows,columns,demand_list,supply_list)
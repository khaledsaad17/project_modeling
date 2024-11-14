

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
supply_list = []
demand_list = []
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

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

                
                
            
#################################################################################################################################

# this code for least cost method
def minimum_value_in_matrix(list_of_rows,rows,columns):
    min_value = float('inf')  # meaning the value is infinity
    r_indix = 0
    c_index = 0
    for i in range(rows):
        for j in range(columns):
            if list_of_rows[i][j]["value"] is None:
                if list_of_rows[i][j]["cells"] < min_value:
                    min_value = list_of_rows[i][j]["cells"]
                    r_indix=i
                    c_index=j
    return {
            "value":min_value,
            "row_index":r_indix,
            "column_index":c_index,
            }

def least_cost_method_fun(list_of_rows,rows,columns,demand_list,supply_list):
    sum=0
    check = True
    while check:
        min_value_info = minimum_value_in_matrix(list_of_rows,rows,columns)
        if min_value_info["value"] is None:
            break
        if demand_list[min_value_info["column_index"]] >= supply_list[min_value_info["row_index"]]:
            list_of_rows[min_value_info["row_index"]][min_value_info["column_index"]]["value"] = supply_list[min_value_info["row_index"]]
            demand_list[min_value_info["column_index"]] -= supply_list[min_value_info["row_index"]]
            supply_list[min_value_info["row_index"]] = 0
            # here we will write code to make the value of row of supply to zero to prevent it form come agian from min function
            for j in range (columns):
                if  list_of_rows[min_value_info["row_index"]][j]["value"] is None:
                    list_of_rows[min_value_info["row_index"]][j]["value"] = 0
            # and here we check for that if the demand and supply are equla
            if demand_list[min_value_info["column_index"]] == supply_list[min_value_info["row_index"]]:
                for i in range(rows):
                    if list_of_rows[i][min_value_info["column_index"]]["value"] is None:
                        list_of_rows[i][min_value_info["column_index"]]["value"] = 0
        else:
            list_of_rows[min_value_info["row_index"]][min_value_info["column_index"]]["value"] = demand_list[min_value_info["column_index"]]
            supply_list[min_value_info["row_index"]] -= demand_list[min_value_info["column_index"]]
            demand_list[min_value_info["column_index"]] = 0
             # here we will write code to make the value of colums of demand to zero to prevent it form come agian from min function
            for i in range(rows):
                if list_of_rows[i][min_value_info["column_index"]]["value"] is None:
                    list_of_rows[i][min_value_info["column_index"]]["value"] = 0
        sum += ( list_of_rows[min_value_info["row_index"]][min_value_info["column_index"]]["value"] * list_of_rows[min_value_info["row_index"]][min_value_info["column_index"]]["cells"] )
        demand_sum=0
        supply_sum=0
        for i in range(rows):
            supply_sum +=supply_list[i]
        for i in range(columns):
            demand_sum += demand_list[i]
        if demand_sum == 0 or supply_sum == 0:
            check = False
    print("Total cost: ", sum)    
    
    


list_of_rows =[]
supply_list = []
demand_list = []
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

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
    
    
    
least_cost_method_fun(list_of_rows,rows,columns,demand_list,supply_list)

#######################################################################################################################




def calculate_the_value_of_minimum(list_of_rows,rows,columns):
    list_of_minimum=[]
    # for each row
    for i in range(rows):
        list_helper=[]
        for j in range(columns):
            if list_of_rows[i][j]["value"] is None:
                list_helper.append(list_of_rows[i][j]["cells"])    
        if list_helper.__len__() == 1:
            list_of_minimum.append({
                "value":list_helper[0],
                "type":'row',
                "index":i
            })
        elif list_helper.__len__() == 0:
            list_of_minimum.append(
                {
                "value":-1,
                "type":'row',
                "index":i
            })
        else:
            list_helper.sort()
            list_of_minimum.append( {
                "value": list_helper[1] - list_helper[0],
                "type":'row',
                "index":i
            })
    # for each column
    for j in range(columns):
        list_helper=[]
        for i in range(rows):
            if list_of_rows[i][j]["value"] is None:
                list_helper.append(list_of_rows[i][j]["cells"])
        if list_helper.__len__() == 1:
            list_of_minimum.append({
                "value":list_helper[0],
                "type":'column',
                "index":j
            })
        elif list_helper.__len__() == 0:
            list_of_minimum.append({
                "value":-1,
                "type":'column',
                "index":j
            })
        else:
            list_helper.sort()
            list_of_minimum.append({
                "value":list_helper[1] - list_helper[0] ,
                "type":'column',
                "index":j
            })
    list_of_minimum.sort(key=lambda x: x['value'])
    return list_of_minimum[-1]

def calculate_the_minimum_of_row(list_of_rows,columns,index):
    min_value={
        "index_row":0,
        "index_column":0,
        "value":float("inf")
    }
    for j in range(columns):
        if list_of_rows[index][j]["value"] is None :
            if list_of_rows[index][j]["cells"] < min_value["value"]:
                min_value = {
                "index_row":index,
                "index_column":j,
                "value":list_of_rows[index][j]["cells"]
            } 
    return min_value
def calculate_the_minimum_of_column(list_of_rows,rows,index):
    min_value={
        "index_row":0,
        "index_column":0,
        "value":float("inf")
    }
    for i in range(rows):
        if list_of_rows[i][index]["value"] is None :
            if list_of_rows[i][index]["cells"] < min_value["value"]:
                min_value = {
                "index_row":i,
                "index_column":index,
                "value":list_of_rows[i][index]["cells"]
            }
    return min_value
            
        
def vogel_method(list_of_rows,rows,columns,demand_list,supply_list):
    check = True
    sum = 0
    while check:
        max_number = calculate_the_value_of_minimum(list_of_rows,rows,columns)
        if max_number["type"] == "row":
            value_will_allocated = calculate_the_minimum_of_row(list_of_rows,columns,max_number["index"])
            if demand_list[value_will_allocated["index_column"]] >= supply_list[value_will_allocated["index_row"]]:
                list_of_rows[value_will_allocated["index_row"]][value_will_allocated["index_column"]]["value"] = supply_list[value_will_allocated["index_row"]]
                demand_list[value_will_allocated["index_column"]] -= supply_list[value_will_allocated["index_row"]]
                supply_list[value_will_allocated["index_row"]] = 0
                for j in range(columns):
                    if  list_of_rows[value_will_allocated["index_row"]][j]["value"] is None:
                        list_of_rows[value_will_allocated["index_row"]][j]["value"] = 0
                
                if demand_list[value_will_allocated["index_column"] == supply_list[value_will_allocated["index_row"]]]:
                    for i in range(rows):
                        if list_of_rows[i][value_will_allocated["index_column"]]["value"] is None:
                            list_of_rows[i][value_will_allocated["index_column"]]["value"] = 0
            else:
                list_of_rows[value_will_allocated["index_row"]][value_will_allocated["index_column"]]["value"] = demand_list[value_will_allocated["index_column"]]
                supply_list[value_will_allocated["index_row"]] -= demand_list[value_will_allocated["index_column"]]
                demand_list[value_will_allocated["index_column"]] = 0
                for i in range(rows):
                        if list_of_rows[i][value_will_allocated["index_column"]]["value"] is None:
                            list_of_rows[i][value_will_allocated["index_column"]]["value"] = 0
        
        elif max_number["type"] == "column":
            value_will_allocated = calculate_the_minimum_of_column(list_of_rows,rows,max_number["index"])
            if demand_list[value_will_allocated["index_column"]] >= supply_list[value_will_allocated["index_row"]]:
                list_of_rows[value_will_allocated["index_row"]][value_will_allocated["index_column"]]["value"] = supply_list[value_will_allocated["index_row"]]
                demand_list[value_will_allocated["index_column"]] -= supply_list[value_will_allocated["index_row"]]
                supply_list[value_will_allocated["index_row"]] = 0
                for j in range(columns):
                    if  list_of_rows[value_will_allocated["index_row"]][j]["value"] is None:
                        list_of_rows[value_will_allocated["index_row"]][j]["value"] = 0
                
                if demand_list[value_will_allocated["index_column"] == supply_list[value_will_allocated["index_row"]]]:
                    for i in range(rows):
                        if list_of_rows[i][value_will_allocated["index_column"]]["value"] is None:
                            list_of_rows[i][value_will_allocated["index_column"]]["value"] = 0
            else:
                list_of_rows[value_will_allocated["index_row"]][value_will_allocated["index_column"]]["value"] = demand_list[value_will_allocated["index_column"]]
                supply_list[value_will_allocated["index_row"]] -= demand_list[value_will_allocated["index_column"]]
                demand_list[value_will_allocated["index_column"]] = 0
                for i in range(rows):
                        if list_of_rows[i][value_will_allocated["index_column"]]["value"] is None:
                            list_of_rows[i][value_will_allocated["index_column"]]["value"] = 0
        sum += ( list_of_rows[value_will_allocated["index_row"]][value_will_allocated["index_column"]]["value"] * list_of_rows[value_will_allocated["index_row"]][value_will_allocated["index_column"]]["cells"] )
        demand_sum=0
        supply_sum=0
        for i in range(rows):
            supply_sum +=supply_list[i]
        for i in range(columns):
            demand_sum += demand_list[i]
        if demand_sum == 0 or supply_sum == 0:
            check = False
    print("Total cost: ", sum)
    

list_of_rows =[]
supply_list = []
demand_list = []
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

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
    

vogel_method(list_of_rows,rows,columns,demand_list,supply_list)
    
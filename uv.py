# this code for least cost method
def minimum_value_in_matrix(matrix,rows,columns):
    min_value = float('inf')  # meaning the value is infinity
    r_indix = 0
    c_index = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j]["value"] is None:
                if matrix[i][j]["cells"] < min_value:
                    min_value = matrix[i][j]["cells"]
                    r_indix=i
                    c_index=j
    return {
            "value":min_value,
            "row_index":r_indix,
            "column_index":c_index,
            }

def least_cost_method_fun(matrix,rows,columns,demand_list,supply_list):
    sum=0
    check = True
    while check:
        min_value_info = minimum_value_in_matrix(matrix,rows,columns)
        if min_value_info["value"] is None:
            break
        if demand_list[min_value_info["column_index"]] >= supply_list[min_value_info["row_index"]]:
            matrix[min_value_info["row_index"]][min_value_info["column_index"]]["value"] = supply_list[min_value_info["row_index"]]
            demand_list[min_value_info["column_index"]] -= supply_list[min_value_info["row_index"]]
            supply_list[min_value_info["row_index"]] = 0
            # here we will write code to make the value of row of supply to zero to prevent it form come agian from min function
            for j in range (columns):
                if  matrix[min_value_info["row_index"]][j]["value"] is None:
                    matrix[min_value_info["row_index"]][j]["value"] = 0
            # and here we check for that if the demand and supply are equla
            if demand_list[min_value_info["column_index"]] == supply_list[min_value_info["row_index"]]:
                for i in range(rows):
                    if matrix[i][min_value_info["column_index"]]["value"] is None:
                        matrix[i][min_value_info["column_index"]]["value"] = 0
        else:
            matrix[min_value_info["row_index"]][min_value_info["column_index"]]["value"] = demand_list[min_value_info["column_index"]]
            supply_list[min_value_info["row_index"]] -= demand_list[min_value_info["column_index"]]
            demand_list[min_value_info["column_index"]] = 0
             # here we will write code to make the value of colums of demand to zero to prevent it form come agian from min function
            for i in range(rows):
                if matrix[i][min_value_info["column_index"]]["value"] is None:
                    matrix[i][min_value_info["column_index"]]["value"] = 0
        sum += ( matrix[min_value_info["row_index"]][min_value_info["column_index"]]["value"] * matrix[min_value_info["row_index"]][min_value_info["column_index"]]["cells"] )
        demand_sum=0
        supply_sum=0
        for i in range(rows):
            supply_sum +=supply_list[i]
        for i in range(columns):
            demand_sum += demand_list[i]
        if demand_sum == 0 or supply_sum == 0:
            check = False
    print("Total cost: ", sum) 
    return matrix   
    
    


matrix =[]
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
    matrix.append(row)
    
for i in range(rows):
    inner=int(input(f"Enter the number of supply from top to down : "))
    supply_list.append(inner)
for i in range (columns):
    inner=int(input(f"Enter the number of demand from left to right "))
    demand_list.append(inner)
    
    
    
matrix_least=least_cost_method_fun(matrix,rows,columns,demand_list,supply_list)


number_of_allocated_cells = 0
for i in range(rows):
    for j in range(columns):
        if matrix_least[i][j]["value"] is not None:
            number_of_allocated_cells +=1
        print(matrix_least[i][j]["value"], end=" ")
    print('\n')










def minimum_ceil_nonallocated(matrix,rows,columns,supply_list,demand_list):
    list_helper =[]
    minimum_value= float('inf')
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j]["value"] is None:
                if matrix[i][j]["cells"] < minimum_value:
                    minimum_value = matrix[i][j]["cells"]
                    list_helper.clear()
                    list_helper.append({"index_row":i,"index_column":j})
                if matrix[i][j]["cells"] == minimum_value:
                    list_helper.append({"index_row":i,"index_column":j})
    if list_helper.__len__() == 1 :
        return list_helper[0]
    else:
        for i in range(list_helper.__len__()):
            if min(supply_list[list_helper[i]["index_row"]],demand_list[list_helper[i]["index_column"]]) >= min(supply_list[list_helper[i+1]["index_row"]],demand_list[list_helper[i+1]["index_column"]]):
                return list_helper[i]
            else:
                return list_helper[i+1]
        
                    

# recurtion for check that is open loop 

# list_row = []
# list_column = []

def check_open_loop(matrix, rows, columns,eps_row,eps_column,index_row,index_column,visited_ceil):
    if eps_row in visited_ceil["index_row"] and eps_column in visited_ceil["index_column"] :
        if visited_ceil["index_row"].__len__() > 2 :    
            return False
        else:
            visited_ceil["index_row"].pop()
            visited_ceil["index_column"].pop()
    
    
    for j in range(columns):
        if matrix[index_row][j]["value"] is not None:
            if  ( i not in visited_ceil["index_row"] ) or ( j  not in visited_ceil["index"] ):
                visited_ceil["index_row"].append(i)
                visited_ceil["index_column"].append(j)
                check_open_loop(matrix, rows, columns,eps_row,eps_column,index_row,j,visited_ceil)
    for i in range (rows):
        if matrix[i][index_column]["value"] is not None:
            if  ( i not in visited_ceil["index_row"] ) or ( j  not in visited_ceil["index"] ):
                visited_ceil["index_row"].append(i)
                visited_ceil["index_column"].append(j)
                check_open_loop(matrix, rows, columns,eps_row,eps_column,i,index_column,visited_ceil)
                    
   
   
def check_close_loop(matrix, rows, columns,eps_row,eps_column,index_row,index_column,visited_ceil):
    if eps_row in visited_ceil["index_row"] and eps_column in visited_ceil["index_column"] :    
        if visited_ceil["index_row"].__len__() > 2 : 
            visited_ceil["checker"]  = True 
            return visited_ceil
        else:
            visited_ceil["index_row"].pop()
            visited_ceil["index_column"].pop()
    
    
    for j in range(columns):
        if matrix[index_row][j]["value"] is not None:
            if  ( i not in visited_ceil["index_row"] ) or ( j  not in visited_ceil["index"] ):
                visited_ceil["index_row"].append(i)
                visited_ceil["index_column"].append(j)
                check_open_loop(matrix, rows, columns,eps_row,eps_column,index_row,j,visited_ceil)
    for i in range (rows):
        if matrix[i][index_column]["value"] is not None:
            if  ( i not in visited_ceil["index_row"] ) or ( j  not in visited_ceil["index"] ):
                visited_ceil["index_row"].append(i)
                visited_ceil["index_column"].append(j)
                check_open_loop(matrix, rows, columns,eps_row,eps_column,i,index_column,visited_ceil)            
        

def filter_of_edges(matrix,rows,columns,n_of_rows,n_of_columns):
    
    final_row=[]
    final_column=[]
    for i in range (max(rows,columns)):
        help_row_matrix = []
        help_column_matrix = []
        if n_of_rows.count(i) > 2:
            for k in range (columns):
                if matrix[i,k]["value"] is not None :
                    help_column_matrix.append({"row" :i, "column" :k})
            final_row.append(help_column_matrix[0]["row"])    
            final_row.append(help_column_matrix[-1]["row"])
            final_column.append(help_row_matrix[0]["column"])    
            final_column.append(help_row_matrix[-1]["column"])
        if n_of_columns.count(i) > 2:
            for k in range (rows):
                if matrix[k,i]["value"] is not None :
                    help_row_matrix.append({"row" :k, "column" :i})
            final_column.append(help_row_matrix[0]["column"])    
            final_column.append(help_row_matrix[-1]["column"])
            final_row.append(help_column_matrix[0]["row"])    
            final_row.append(help_column_matrix[-1]["row"])
    return {"row":final_row,"column":final_column}    

def uv_method(matrix , rows,columns,supply_list,demand_list,number_of_allocated_cells):
    r=[]
    c=[]
    while (rows + columns ) - 1 > number_of_allocated_cells:
        minumum_ceil=minimum_ceil_nonallocated(matrix,rows,columns,supply_list,demand_list)
        matrix[minumum_ceil["index_row"]][minumum_ceil["index_column"]]["value"] = float('inf')
        check_value=check_open_loop(matrix,rows,columns,minumum_ceil["index_row"],minumum_ceil["index_column"],minumum_ceil["index_row"],minumum_ceil["index_column"],{"index_row":[], "index_column":[],"checker":False})    
        if check_value != False:
            number_of_allocated_cells +=1
        else:
            # matrix[minumum_ceil["index_row"]][minumum_ceil["index_column"]]["value"] = None
            r.append(minumum_ceil["index_row"])
            c.append(minumum_ceil["index_column"])    
    
    for i in range (r.__len__()):
        for j in range(c.__len__()):
            matrix[r[i]][c[i]]["value"] = None
    
            
    u=[{
      "u":0,
    }]
    v=[]
    for i in range(rows):
        if i != 0:
            u.append({"u":None})
    for i in range(columns):
        v.append({"v":None})
    check_that_all_u_and_v_calculated = 0
    while check_that_all_u_and_v_calculated <= number_of_allocated_cells:
        for i in range (rows):
            for j in range(columns):
                if matrix[i][j]["value"] is not None:
                    if u[i]["u"] is not None and v[j]["v"] is None:
                        check_that_all_u_and_v_calculated +=1
                        v[j]["v"] = matrix[i][j]["ceils"] - u[i]["u"]
                    if u[i]["u"] is None and v[j]["v"] is not None:
                        check_that_all_u_and_v_calculated +=1
                        u[i]["u"] = matrix[i][j]["ceils"] - v[j]["v"]
    
    p=[]
    for i in range (rows):
        for j in range(columns):
            if matrix[i][j]["value"] is None:
                value = u[i]["u"] + v[j]["v"] + matrix[i][j]["ceils"]
                p.append({"p": value,
                          "index_row":i,
                          "index_column":j
                          })
    p.sort(key=lambda x: x["p"])
    if p[-1]["p"] > 0:
        matrix[p[-1]["index_row"]][p[-1]["index_column"]]["value"] = float('inf')
        check_value=check_close_loop(matrix, rows,columns,p[-1]["index_row"],p[-1]["index_column"],p[-1]["index_row"],p[-1]["index_column"],{"index_row":[], "index_column":[]})
        if check_value["checker"] == True:
            filtered_data=filter_of_edges(matrix,rows,columns,check_value["index_row"],check_value["index_column"])
            




uv_method(matrix,rows,columns,demand_list,supply_list,number_of_allocated_cells)







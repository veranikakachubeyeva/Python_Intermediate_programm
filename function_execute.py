from task2_counter_occuriencies import *


d = get_data_from_file(sys.argv) 
results =  count_occuriencies(d)


if results !=None:
    print(results)
else:
    print("File is empty")
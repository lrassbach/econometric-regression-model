###csv data reader. presents .csv data in a column-row format

def csv_run():
    

    import csv

    name = input('Enter exact file name:')

    csv_file = open('%s' % name, 'r')

    csv_reader = csv.reader(csv_file)
    new_dic = {}
    i = 0
    for item in csv_reader:
        i += 1
        new_dic[i] = item
    print(new_dic)
    return(csv_reader)  
    
    

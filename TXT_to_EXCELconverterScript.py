import xlrd, xlwt

input_file = raw_input("Please enter file name with extension: ")
file1 = open(input_file,"r")

output_file = raw_input("Please enter output file name without extension: ")


workbook = xlwt.Workbook()
worksheet = workbook.add_sheet(output_file+'.xls')

parse_list =[]

avg_perf_sum = 0

row = 0

new_line = 1

coloum = 0

firstLine = 1

while(new_line):
    
    new_line = file1.readline(28)
 
    if(row%65530 == 0):
        row = 0
        worksheet.col(coloum).width = 256 * (len("Name") + 1)
        worksheet.write(row, coloum, "Name")
        name = coloum

        coloum=coloum+1
        worksheet.col(coloum).width = 256 * (len("Time    ") + 1)
        worksheet.write(row, coloum, "Time")
        time = coloum

        coloum=coloum+1
        worksheet.col(coloum).width = 256 * (len("Performance    ") + 1)
        worksheet.write(row, coloum, "Performance")
        performance = coloum
        
        coloum=coloum+1
        worksheet.col(coloum).width = 256 * (len("Avg Performance  ") + 1)
        worksheet.write(row, coloum, "Avg Performance")
        avg_performance = coloum

        coloum=coloum+1
        worksheet.col(coloum).width = 256 * (len("New Performance  ") + 1)
        worksheet.write(row, coloum, "New Performance")
        new_performance = coloum

        coloum=coloum+1
        worksheet.col(coloum).width = 256 * (len("           ") + 1)
        worksheet.write(row, coloum, "        ")

        coloum=coloum+1
        row = row + 1


    if(len(new_line) > 10):
        
        parse_list = new_line.split("=")

        if(len(parse_list)!=2):
            print "Unexpected string:",new_line
            continue

        #print "list:",parse_list

        worksheet.row(row).height_mismatch = True
        worksheet.row(row).height = 256*3
        worksheet.col(name).width = 256 * (len(parse_list[0]) + 1)
        worksheet.write(row, name, parse_list[0])
        worksheet.col(time).width = 256 * (len(parse_list[1]) + 1)
        worksheet.write(row, time, float(parse_list[1]))

         
                
        if(parse_list[0]=='cmd_time (real) '):
            performance_value = (1024*1024)/((float(parse_list[1]))*1000)
            worksheet.write(row, performance, performance_value)
            workbook.save(output_file+'.xls')

        if(parse_list[0]=='rand_write (real) '):
            next_perf = 16/(float(parse_list[1]))
            worksheet.write(row, performance, next_perf)
            workbook.save(output_file+'.xls')

        if(parse_list[0]=='rd_cmd_time (real) '):
            performance_value = (1024*1024)/((float(parse_list[1]))*1000)
            worksheet.write(row, performance, performance_value)
            workbook.save(output_file+'.xls')
            
        if(parse_list[0]=='rand_read (real) '):
            next_perf = 16/(float(parse_list[1]))
            worksheet.write(row, performance, next_perf)
            workbook.save(output_file+'.xls')

        if(((parse_list[0] == 'cmd_time (real) ') or (parse_list[0] == 'rd_cmd_time (real) ')) and firstLine>1):
             worksheet.row(nrow).height_mismatch = True
             worksheet.row(nrow).height = 256*3
             #worksheet.col(avg_performance).width = 256 * ("avg_perf_sum" + 1)
             worksheet.write(nrow, avg_performance, avg_perf_sum)
             
             new = (1.1*1024*1024)/(avg_perf_sum*1000)
             #worksheet.col(new_performance).width = 256 * ("new" + 1)
             worksheet.write(nrow, new_performance, new)
             avg_perf_sum = 0
             new = 0
             if(firstLine>20):
                 firstLine = 2


        nrow = row         
        row=row + 1
        avg_perf_sum = avg_perf_sum + float(parse_list[1])
        firstLine = firstLine + 1     
          
workbook.save(output_file+'.xls')
file1.close()











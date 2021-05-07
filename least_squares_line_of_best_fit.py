### WILL FIND THE LINE OF BEST FIT WITH THE LEAST SQUARES METHOD.

def line_of_best_fit():
    data_points = []
    intake_data = True
    
    while intake_data:
        floater_X = float(input('Choose an X value >  '))
        floater_Y = float(input('Choose a Y value >  '))
        data_points.append([floater_X, floater_Y])
        again = input('Do you want to do more (y or n) >  ')
        
        if again == 'n':
            intake_data = False
            
    m = find_slope(data_points)
    b = find_B(data_points, m)
    
    print('Your line of best fit is: ')
    print('Y = ' + str(round(m, 2)) + 'x + (' + str(round(b, 2)) +')')
        
def find_B(data_points, m):
    X, Y = 0, 0
    n = len(data_points)
    
    for i in range(len(data_points)):
        X += data_points[i][0]
        Y += data_points[i][1]
        
    b = (Y - (m * X)) / n
    
    return b

def find_slope(data_list):
    sumXY, sumX, sumY, sumX2 = 0, 0, 0, 0
    n = len(data_list)
    
    for i in range(len(data_list)):
        sumXY += data_list[i][0] * data_list[i][1]
        sumX += data_list[i][0]
        sumY += data_list[i][1]
        sumX2 += (data_list[i][0] ** 2)
        
    m = (sumXY - ((sumX * sumY) / n)) / (sumX2 - (sumX ** 2) / n)
    
    return m

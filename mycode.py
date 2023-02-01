import sys
from collections import defaultdict, deque

class logger:
    "simulation of logging"
    def error(s):
        print(s)
    def info(s):
        print(s)

def calculate(filename="transactions.csv"):

    try:
        points_to_spend = int(sys.argv[1])
    except:
        logger.error("valid input should be like 'python3 mycode.py 5000'")
        exit(0)

    '''
    points_to_spend: given value to spend from argv
    total_points_of_payer: a dictionary record total points of each payer, which serve as return answer
    history: transactions history from csv file as list format
    '''
    total_points_of_payer = defaultdict(int)
    history = []
    '''
    data processing
    '''
    try:
        with open(filename) as fd:
            for line in fd.readlines()[1:]:
                payer, points, timestamp = line.split(",")
                points = int(points)
                total_points_of_payer[payer]+=points
                history.append([payer, points, timestamp])
    except:
        logger.error("invalid format in transaction.csv file or missing transaction.csv")
        exit(0)
    
    '''
    Expect to applying points with the first time-stamp, sort the "history" 
    list in ascending order base on time-stamp. Then, formulate "history" 
    as a queue (deque, in python implementation with popleft())
    '''
    history.sort(key=lambda x:x[2])
    history = deque(history)

    '''
    The following "while loop" part greedly spent the points with earlier time-stamp.
    The loop exits with 2 cases:
        1. spend all points given by argv
        2. there is no enough points to spent to reach the target points(points_to_spend)
    In each iteration,
        1. if the points is negative, add to points_to_spend
        2. if the points is positive,
            a. if the total_points of the payer become negative after spending points of this time-stamp
               we should only spend partial points to maintain the balance>=0
               (The problem doen't clearify the definition of negative points. As I consider a value 
               of total points at first, the total_points might be less than points in each time-stamp
               be pop out from the queue)
            b. if the total_points of the payer can cover the value of points of current time-stamp
                i. if points of current time stamp is less than points_to_spend, all points from current 
                   time-stamp could be apply
                ii. if the points of current time stamp is bigger than points_to_spend, only partial points of
                    current time-stamp need to be spent
                (the situation of points equal to points_to_spend could be covered in the following implemtation)
            For case a and b, they could be formulate as "cost = min(total_points_of_payer[payer], points, points_to_spend)"
            since we only need to condiser the smallest value of these variables (to spend) to satisfy these condition
    '''
    while points_to_spend > 0 and len(history) > 0:
        payer, points, _ = history.popleft()
        if points < 0:
            points_to_spend-=points
            total_points_of_payer[payer]-=points
            cost = points
        else:
            cost = min(total_points_of_payer[payer], points, points_to_spend)
            points_to_spend-=cost
            total_points_of_payer[payer]-=cost

    '''
    since the output expect to be json format, change defaultdict to be dictionary
    if all the transaction can't cover up the "points_to_spend" value, output it 
    on stdout
    '''
    total_points_of_payer = dict(total_points_of_payer)
    print(total_points_of_payer)
    if points_to_spend > 0:
        logger.info('Points left (not be spent):'+str(points_to_spend))
    return total_points_of_payer
    

if __name__ == "__main__":
    result = calculate('transactions.csv')


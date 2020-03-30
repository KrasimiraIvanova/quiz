# def function with 3 arg according info
def assingment(matrix, start, end):
    steps = [start]
    x,y = start
    while True:
        if (x,y) == end:
            return len(steps)-1
        
        top = x-1 >= 0 and not matrix[x-1][y] and (x-1,y) not in steps
        left = y-1 >= 0 and not matrix[x][y-1] and (x,y-1) not in steps
        bottom = x+1 < len(matrix) and not matrix[x+1][y] and (x+1,y) not in steps
        right = y+1 < len(matrix[x]) and not matrix[x][y+1] and (x, y+1) not in steps

        if x >= end[0]:
            if y >= end[1]:
                if top and (x > end[0] or not bottom) :  # can go top
                    x = x-1
                    steps.append((x,y))
                elif left and (y > end[1] or not right) :  # can go left
                    y = y-1
                    steps.append((x,y))
                elif right and (y < end[1] or not left):  # can go right
                    y = y+1
                    steps.append((x,y))
                elif bottom and (x < end[0] or not top):  # can go bottom
                    x = x+1
                    steps.append((x,y))
            else:
                if top and (x > end[0] or not bottom) :  # ca go top
                    x = x-1
                    steps.append((x,y))
                elif right and (y < end[1] or not left):  # can go right
                    y = y+1
                    steps.append((x,y))
                elif left and (y > end[1] or not right) :  # can go left
                    y = y-1
                    steps.append((x,y))
                elif bottom and (x < end[0] or not top):  # can go bottom
                    x = x+1
                    steps.append((x,y))
        else:
            if y >= end[1]:
                if bottom and (x < end[0] or not top):  # can go bottom
                    x = x+1
                    steps.append((x,y))
                elif left and (y > end[1] or not right) :  # can go left
                    y = y-1
                    steps.append((x,y))
                elif right and (y < end[1] or not left):  # can go right
                    y = y+1
                    steps.append((x,y))
                elif top and (x > end[0] or not bottom) :  # can go top
                    x = x-1
                    steps.append((x,y))
            else:
                if bottom and (x < end[0] or not top):  # can go bottom
                    x = x+1
                    steps.append((x,y))
                elif right and (y < end[1] or not left):  # can go right
                    y = y+1
                    steps.append((x,y))
                elif left and (y > end[1] or not right) :  # can go left
                    y = y-1
                    steps.append((x,y))
                elif top and (x > end[0] or not bottom) :  # can go top
                    x = x-1
                    steps.append((x,y))
                    
def steps():
    matrix = [
        [False, False,  False,  False],
        [True,  True,   False,  True],
        [False, False,  False,  False],
        [False, False,  False,  False]
    ]   
    start = (3, 0)
    end = (0, 0)
    return True

if steps():
  print("7")
else:
  print("None")

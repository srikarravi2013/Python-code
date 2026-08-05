from collections import deque

def generate_a_list():
    x = []
    z = 1
    
    while True:
        try:
            y = int(input(f"what is number {z} in the list (or letters to stop): "))
            x.append(y)
            z += 1 
        except ValueError:
            break
    return x
    

def rotate_list(x,y):
    d = deque(x)
    d.rotate(y) 
    rotated_list = list(d) 
    print(rotated_list)
    StopIteration

rotate_list(generate_a_list(),1)

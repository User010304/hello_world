import time
start_time= time.time()
def fun():
    a=2
    b=5
    c=a+b
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken)
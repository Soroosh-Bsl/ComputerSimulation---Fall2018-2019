import random, sys


def X(num, prob, array, val):
    for i in range(int(num * prob)):
        done = False
        while not done:
            rand = random.randint(0, num-1)
            if array[rand] == -1:
                done = True
                array[rand] = val


def create_clients(num, p_interval, p_work_time, interval_values, work_time_values):
    interval = [-1] * num
    X(num, p_interval[0], interval, interval_values[0])
    X(num, p_interval[1], interval, interval_values[1])
    X(num, p_interval[2], interval, interval_values[2])
    X(num, p_interval[3], interval, interval_values[3])
    X(num, p_interval[4], interval, interval_values[4])

    work_time = [-1] * num
    X(num, p_work_time[0], work_time, work_time_values[0])
    X(num, p_work_time[1], work_time, work_time_values[1])
    X(num, p_work_time[2], work_time, work_time_values[2])
    X(num, p_work_time[3], work_time, work_time_values[3])
    X(num, p_work_time[4], work_time, work_time_values[4])

    return interval, work_time


number = 200
print("Interval time values :")
interval_values = list(map(float, input().split()))
print("Interval time probabilities")
interval_prob = list(map(float, input().split()))
print("Work time values")
work_time_values = list(map(float, input().split()))
print("Work time probabilities")
work_time_prob = list(map(float, input().split()))
interval, work_time = create_clients(number, interval_prob, work_time_prob, interval_values, work_time_values)
entrance = [0]
for i in range(1, number):
    entrance.append(entrance[i-1] + interval[i])

entrance_pointer = 0
end_estimation = 0
time = 0
queue = []
busy = False
waited = []
endded = 0

while True:
    event_happend = False
    if time == end_estimation:
        if busy == True:
            endded += 1
            event_happend = True
        busy = False
    if entrance_pointer < len(entrance) and entrance[entrance_pointer] == time:
        queue.append(entrance_pointer)
        entrance_pointer += 1
        event_happend = True
    if not busy and len(queue) > 0:
        end_estimation = time + work_time[queue[0]]
        waited.append(time - entrance[queue[0]])
        busy = True
        del queue[0]
        event_happend = True
    if event_happend:
        print("Time = ", time, ", ", "LQ(t) = ", len(queue), ", ", "Busy = ", busy, ", ", "(D,", end_estimation if busy else "NOTHING", "), ", "(A,", entrance[entrance_pointer] if entrance_pointer < len(entrance) else "NOTHING", ")", sep="")

    if endded == number:
        break
    minimum = []
    minimum += [end_estimation if busy else sys.maxsize]
    minimum += [entrance[entrance_pointer] if entrance_pointer < len(entrance) else sys.maxsize]
    time = min(minimum)

print("Waiting AVG =", sum(waited)/len(work_time), "Working AVG =", sum(work_time)/len(entrance))

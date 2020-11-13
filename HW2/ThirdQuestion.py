import math
from random import *
import sys

print("================================")
print("Question 3")
print("================================")


def exp_random(u, lambda_input):
    result = []
    for i in range(len(u)):
        result.append(F_inverse_exp(lambda_input, u[i]))
    return result


def F_inverse_exp(lambda_exp, u):
    return -1/lambda_exp * (math.log(1-u))


def simulation(interval, work_time, number):
    entrance = [0]
    for i in range(1, number):
        entrance.append(entrance[i - 1] + interval[i])

    entrance_pointer = 0
    end_estimation = 0
    time = 0
    queue = []
    busy = False
    waited = []
    endded = 0
    L = 0
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
            print("Time = ", time, ", ", "LQ(t) = ", len(queue), ", ", "Busy = ", busy, ", ", "(D,",
                  end_estimation if busy else "NOTHING", "), ", "(A,",
                  entrance[entrance_pointer] if entrance_pointer < len(entrance) else "NOTHING", ")", sep="")

        if endded == number:
            L /= time
            break
        minimum = []
        minimum += [end_estimation if busy else sys.maxsize]
        minimum += [entrance[entrance_pointer] if entrance_pointer < len(entrance) else sys.maxsize]
        L += len(queue) * (min(minimum)-time)
        time = min(minimum)

    print("Waiting AVG =", sum(waited) / len(work_time), "     Working AVG =", sum(work_time) / len(entrance), "    L(Q) AVG =", L)


simulation(exp_random([random() for i in range(100)], 1/90), exp_random([random() for i in range(100)], 1/75), 100)

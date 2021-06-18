"""
Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.

https://en.wikipedia.org/wiki/Clock_angle_problem

Formulas:
Angle of Hour hand, AOH = .5 * (60 * H + M)
Angle of Minute hand, AOM = 6 * M
Angle between Hour and Minute hand, AOD(delta) = |AOH - AOM|
"""

def calcAngle(h, m):
    aoh = .5 * ((60 * h) + m)
    aoh = min(aoh, abs(360-aoh))

    aom = 6 * m

    return abs(aoh - aom)

print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
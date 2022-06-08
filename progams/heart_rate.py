"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

# Get User to input age
userAge = input('What is your age?: ')

#convert Age from string to int
age = int(userAge)

#calculate maximum heart rate
maxHeartRate = 220 - age

#calculate upper heart rate range
upperRange = maxHeartRate * .85

#calculate lower heart rate range
lowerRange = maxHeartRate * .65

print('When you exercise to strengthen your heart, you should')
print(f'keep your heart rate between {lowerRange:.0f} and {upperRange:.0f}')
print('beats per minute.')

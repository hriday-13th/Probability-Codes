# Coupon Collector Problem

# Create a program that models the coupon collector problem. In this problem, you have a set of 'n' distinct coupons,
# and each time you collect a coupon, it's equally likely to be any of the 'n' types. Calculate the expected number of
# coupons you need to collect to complete the set.

import random

n = int(input("Enter the number of coupons to be collected: "))

count = 0

collected = set()

while set(collected) != set(range(n)):
    collected.add(random.randint(0, n-1))
    count += 1

print(count)

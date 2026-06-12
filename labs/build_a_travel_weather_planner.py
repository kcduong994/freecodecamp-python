distance_mi = 100
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

# If distance is a falsy value:
# You should print False.
if not distance_mi:
    print(False)

# If the distance is 1 mile or less:
# Print True only if it is not raining
# Otherwise, print False.
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)   

# If the distance is between 1 mile (excluded) and 6 miles (included):
# Print True only if the person has a bike
# and it is not raining.
# Otherwise, print False.

elif 1 < distance_mi <=6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)    

# If the distance is greater than 6 miles:
# Print True if the person has a car
# or has a ride app share.
# Otherwise, print False.

elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)    

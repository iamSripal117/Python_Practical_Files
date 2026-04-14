##def gym_cost(months):
##    if months < 0:
##        return "invalid input"
##    elif months == 0:
##        return 0
##    elif months == 1:
##        return 2000
##    elif months == 2 or months == 3:
##        return 5000
##    elif 4 <= months <= 6:
##        return 9000
##    elif months == 9:
##        return 12000
##    elif months == 12:
##        return 15000
##    else:
##        return "Error"
##
##
### Testing
##print(gym_cost(3))   # 5000
##print(gym_cost(5))   # 9000
##print(gym_cost(-1))  # invalid input


def validate_transactions(n, transactions):
    seen = set()
    prev_time = None

    for i in range(n):
        sender, receiver, time, amount = transactions[i]
        time = int(time)

        # Rule 1: Duplicate check
        if (sender, receiver) in seen:
            print("ERROR DUPLICATION TRANSACTION")
            return
        seen.add((sender, receiver))

        # Rule 2: Time difference check
        if prev_time is not None:
            if time - prev_time > 60:
                print("FRAUD DETECTED")
                return

        prev_time = time

    print("ALL TRANSACTION ARE VALID")

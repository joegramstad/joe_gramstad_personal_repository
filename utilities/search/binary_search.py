## Conditions:
    ## search = sorted array
    ## payload = value to search for
## Best Runtime = O(1)
## Worst Runtime = O(log n)
## Average Runtime = O(log n) 
## Space = 

def binary_search(search, payload):
    low = 0
    high = len(search) - 1

    while low <= high:
        mid = (high + low) // 2
        guess = search[mid]
        if payload == guess:
            return mid
        elif payload < guess:
            high = mid - 1
        elif payload > guess:
            low = mid + 1

    return None
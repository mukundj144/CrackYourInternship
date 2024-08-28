def can_we_place(stalls, dist, cows):
    cnt_cows = 1
    last = stalls[0]
    
    for i in range(1, len(stalls)):
        if stalls[i] - last >= dist:
            cnt_cows += 1
            last = stalls[i]
        if cnt_cows >= cows:
            return True
    
    return False

def aggressiveCows(stalls, k):
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    
    while low <= high:
        mid = (low + high) // 2
        if can_we_place(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    
    return high

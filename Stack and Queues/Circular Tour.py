class Solution:
    
    def tour(self, lis, n):
        total_petrol = 0
        total_distance = 0
        current_surplus = 0
        start_index = 0
        
        for i in range(n):
            petrol = lis[i][0]
            distance = lis[i][1]
            
            total_petrol += petrol
            total_distance += distance
            current_surplus += petrol - distance
            
            # If current surplus is negative, reset the starting index
            if current_surplus < 0:
                start_index = i + 1
                current_surplus = 0
        
        # Check if total petrol is greater than or equal to total distance
        if total_petrol >= total_distance:
            return start_index
        else:
            return -1

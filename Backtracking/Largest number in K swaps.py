class Solution:
    
    def findMaximumNum(self, s, k):
        def swap(string, i, j):
            # Convert string to list to perform swap
            char_list = list(string)
            char_list[i], char_list[j] = char_list[j], char_list[i]
            return ''.join(char_list)
        
        def findMaxRecursively(string, k, maxm, idx):
            # Base case: if no swaps left or entire string is checked
            if k == 0 or idx == len(string):
                return
            
            # Find the maximum digit from idx to end of the string
            max_digit = max(string[idx:])
            
            # If the max_digit is not greater than the current digit at idx, no swap needed
            if max_digit != string[idx]:
                for i in range(idx + 1, len(string)):
                    if string[i] == max_digit:
                        # Swap the current digit with the found max_digit
                        new_string = swap(string, idx, i)
                        
                        # Update maximum number found so far
                        if new_string > maxm[0]:
                            maxm[0] = new_string
                        
                        # Recurse with remaining swaps and move to next index
                        findMaxRecursively(new_string, k - 1, maxm, idx + 1)
        
            # Recurse without swapping for the next index
            findMaxRecursively(string, k, maxm, idx + 1)
        
        # Initialize maxm to keep track of the maximum number
        maxm = [s]
        
        # Start the recursive function
        findMaxRecursively(s, k, maxm, 0)
        
        return maxm[0]

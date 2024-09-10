class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:  # If n is a single digit, return n
            return n
        
        base = 9  # Set the base value for the digit count
        digits = 1  # Set the initial number of digits to 1
        while n > base * digits:
            n -= base * digits  # Subtract the count of digits from n
            base *= 10  # Increase the base value by a factor of 10
            digits += 1  # Increase the number of digits by 1
            
        num = 10 ** (digits - 1) + (n - 1) // digits  # Calculate the number where the nth digit is located
        idx = (n - 1) % digits  # Calculate the index of the nth digit in the number
        
        return int(str(num)[idx])  # Return the nth digit as an integer
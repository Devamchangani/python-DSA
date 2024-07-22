class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
    
        # Mapping of digits to corresponding letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    
        # Convert digits to corresponding letters
        letters = [phone_map[digit] for digit in digits if digit in phone_map]
        
        # Generate all combinations using Cartesian product
        combinations = [''.join(combo) for combo in product(*letters)]
        
        return combinations
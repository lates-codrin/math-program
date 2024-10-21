
import math
def is_prime(x: int) -> bool:
        """Determines if a number `x` is prime.
        
        Args:
            x (int): The number to check for primality.

        Returns:
            bool: True if `x` is prime, False otherwise.
        """
        if x == 2:
            return 1
        elif x < 2 or x % 2 == 0:
            return 0
        else:
            for d in range(3, math.isqrt(x) + 1, 2):
                if x % d == 0:
                    return 0
        return 1
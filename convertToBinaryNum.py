class BinaryNum:
    def convertBinary(self, N):
        moduloOp = 0
        arr = [0] * (N.bit_length() if N > 0 else 1)
        
        for i in range(len(arr)):
            moduloOp = N % 2
            arr[i] = moduloOp
            N = N // 2
        # Return the binary representation in conventional order (MSB first)
        return arr[::-1]
# Example usage:
obj = BinaryNum()
result = obj.convertBinary(5)


print(result)  # Output the binary representation as a list (MSB first)

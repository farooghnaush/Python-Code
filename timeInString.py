class TimeInString:
    def solution(self, T):
        """
        Converts an integer T representing seconds into a formatted string
        showing hours, minutes, and seconds.

        Parameters:
        T (int): The time duration in seconds.

        Returns:
        str: A string representing the time in 'HhMmSs' format.
        """
        # Implement your solution here
        if T >= 3600:
            hour = T // 3600
            remhour = T % 3600
            min = remhour // 60
            sec = remhour % 60
            b = str(hour) + "h" + str(min) + "m" + str(sec) + "s"
        elif T >= 60:
            sec = T % 60
            min = T // 60
            b = str(min) + "m" + str(sec) + "s"
        else:
            b = str(T) + "s"
        
        return b

# Example usage:
time_converter = TimeInString()
print(time_converter.solution(3661))  # Output: "1h1m1s"
print(time_converter.solution(61))     # Output: "1m1s"
print(time_converter.solution(5))      # Output: "5s"
# Example usage:
if __name__ == "__main__":  
    time_converter = TimeInString()
    T = 3661  # total seconds
    print(time_converter.solution(T))  # Output the formatted time "1h1m1s"
# Python Program that takes a positive floating-point number as input and outputs an approximation of its square root
#author:Regina Fennessy


def squareRoot(n, l) :
 
    # Assigning 
    <tt>sqrt</tt = n
 
    # To count the number of iterations
    count = 0
 
    while (1) :
        count += 1
 
        # Calculate more closed x
        root = 0.5 * (<tt>sqrt</tt + (n / <tt>sqrt</tt))
 
        # Check for closeness
        if (abs(root - <tt>sqrt</tt) < l) :
            break
 
        # Update root
        <tt>sqrt</tt = root
 
    return root
 
# Driver code
if __name__ == "__main__" :
 
    num = float(input("Please enter a positive number:"))
    l = 0.00001
 
    print("The square root of 14.5 is approx.  "  squareRoot(num, l))
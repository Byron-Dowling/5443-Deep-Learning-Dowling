""" 
    Names:      Byron Dowling and Israel Olaemimimo
    Class:      Deep Learning
    Semster:    Summer 1 2022
    Date:       6/2/22
    Assignment: Homework 1

    Original Assignment Description: 

            Write a python program that will compute the mean, variance and standard deviation of a group of
            samples entered by the user.

            Your program must:
            1) Allow the user to enter the samples (one at a time)
            2) Populate the X array until the user decided not to enter more samples.
            3) Call a function that will compute the mean. The array of samples X must be passed to the
                function, which will return as a result the value of the corresponding mean.
                https://www.mathsisfun.com/mean.html
            4) Once the mean has been estimated the program must proceed to invoke a second function,
                which will compute the variance using the SAMPLE formula.
                https://www.mathsisfun.com/data/standard-deviation.html
            5) Next, the variance has to be computed by a third function.
            6) Last but not list, a final and 4th function will be invoked to print the output on screen as follows:
                Make sure that you make use of the formatting explained in class (check your jupyter
                notebooks)

    Program Notes:

            - The goal of this program is to calculate the Standard Deviation of a dataset that is entered in
              by the end user, giving them complete control of how many numbers are in the data set.
            
            - A function is used to populate the data set which upon completeion, the standard deviation process
              is handled by computing the mean, the variances, squaring each variance, adding them all together
              and then taking the square root of that to find the standard deviation.

            - Additionally, because we are using the SAMPLE formula for Standard Deviation, we are using N-1 instead
              of N in our calculations.
"""

import math             ## For the Square Root Function


"""
    Function Name: insertNumbers
    Passed Parameters: No passed parameters
    Returns: a List of numbers

    Details: 

        To handle creating the dataset, a while loop is utilized that is set to True, essentially
        an infinite loop, that will allow the user to continue to type in numbers that are casted
        and then appended to the list of numbers. If invalid input is entered, it is essentially
        ignored and then the loop executes again. Once the user is done, they will simply type in
        STOP to break out of the loop.

        One final detail is that input is initially captured as a string, then we check if it is
        numeric, this would tell us that a number is entered which makes it safe for us to cast it
        as a float. If the string is not numeric and isn't 'STOP' then we know it's invalid input.
"""

def insertNumbers():

    numbers = []

    while(True):

        print("Please enter a number to add to the list.")
        print("To stop adding numbers, type STOP")

        num = str(input())

        if num.isnumeric():
            num = float(num)
            numbers.append(num)
            print()

        elif num == 'STOP':
            break

        else:
            print("Invalid input, please try again.\n")

    return numbers


"""
    Function Name: computeMean
    Passed Parameters: List of Numbers
    Returns: Float

    Details: 

        This is a straightforward section of code. We will loop through the passed in list
        of numbers and we will calculate the running total and then divide it by the length
        of the list to calculate the mean.

        The mean is then returned to be used later.
"""

def computeMean(nums):
    
    mean = float()
    RT = 0

    for num in nums:

        RT = RT + num

    mean = RT / len(nums)

    return mean


"""
    Function Name: getVariants
    Passed Parameters: List of Numbers, Float
    Returns: List of numbers

    Details: 

        This function is responsible for calculating the variances of each number which is to
        say that we will take each number from our original list and subtract the mean from it
        and then log those results in a separate list. Additionally, we are formating the results
        to restrict to two decimal places.

        Once complete, the list of variances is retured for future use.
"""

def getVariants(nums, mean):

    variances = []

    for num in nums:

        var = float()
        var = num - mean
        var = float("{:.2f}".format(var))
        variances.append(var)

    return variances


"""
    Function Name: computeVariance
    Passed Parameters: List of Variances
    Returns: Float

    Details: 

        This function loops through the list of variances and squares each result and keeps 
        track of the running total. We will then divide it by N-1 per the SAMPLE strategy for
        Standard Deviation.

        The result is returned for future use.
"""

def computeVariance(vars):

    varSqrSum = float()

    for v in vars:

        v = v**2
        varSqrSum = varSqrSum + v

    variance = (varSqrSum / (len(vars) - 1))

    return variance


"""
    Function Name: getStandardDeviation
    Passed Parameters: Float
    Returns: Float

    Details: 

        This function takes the previously calculated variance and then takes the square
        root of this value which is our Standard Deviation.

        The value si returned so it can be passed to the print function
"""

def getStandardDeviation(variance):
     
     stdVar = math.sqrt(variance)
     return stdVar



"""
    Function Name: printResults
    Passed Parameters: List, List, Float, Float, Float
    Returns: None

    Details: 

        This is a utility function that is used to print the results of our standard deviation
        data set in the specified format. This function makes use of string formatting similar to
        setw in C++ where we speciy the width of the formatted string and specify using < > to 
        which direction the text is aligned, left or right.
"""

def printResults(nums, vars, mean, variance, stdDev):

    xiSum = 0
    xbarSqrtSum = 0

    for num in nums:

        xiSum = xiSum + num

    
    i = "{0:<8}".format("i")
    xi = "{0:<10}".format("xi")
    xbar = "{0:<20}".format("(xi-xbar)")
    xbarSqrt = "{0:<30}".format("(xi-xbar) ^ 2")
    print()
    print(i, xi, xbar, xbarSqrt)
    print('----------------------------------------------------------------')

    for index in range(len(nums)):

        sample = "{0:<8}".format(index+1)
        xiVal = "{0:<10}".format(nums[index])
        xV = float("{:.2f}".format(vars[index]))
        xbarVal = "{0:<20}".format(xV)


        v = float("{:.2f}".format(vars[index]**2))
        xbarSqrtSum = xbarSqrtSum + v
        xbarSqrtVal = "{0:<30}".format(v)
        print(sample, xiVal, xbarVal, xbarSqrtVal)

    print('----------------------------------------------------------------')
    print("{0:>20}".format(f'SUM: {xiSum}'), "{0:>33}".format(f'SUM: {xbarSqrtSum}'))
    print()
    print(f'There are {len(nums)} Samples')
    print("The mean for this set of samples is:", float("{:.2f}".format(mean)))
    print("The variance for this set of samples is:", float("{:.2f}".format(variance)))
    print("The Standard Deviation of this Sample is:", float("{:.2f}".format(stdDev)))


"""
    $$\      $$\           $$\                 $$$$$$$\  $$\                     $$\       
    $$$\    $$$ |          \__|                $$  __$$\ $$ |                    $$ |      
    $$$$\  $$$$ | $$$$$$\  $$\ $$$$$$$\        $$ |  $$ |$$ | $$$$$$\   $$$$$$$\ $$ |  $$\ 
    $$\$$\$$ $$ | \____$$\ $$ |$$  __$$\       $$$$$$$\ |$$ |$$  __$$\ $$  _____|$$ | $$  |
    $$ \$$$  $$ | $$$$$$$ |$$ |$$ |  $$ |      $$  __$$\ $$ |$$ /  $$ |$$ /      $$$$$$  / 
    $$ |\$  /$$ |$$  __$$ |$$ |$$ |  $$ |      $$ |  $$ |$$ |$$ |  $$ |$$ |      $$  _$$<  
    $$ | \_/ $$ |\$$$$$$$ |$$ |$$ |  $$ |      $$$$$$$  |$$ |\$$$$$$  |\$$$$$$$\ $$ | \$$\ 
    \__|     \__| \_______|\__|\__|  \__|      \_______/ \__| \______/  \_______|\__|  \__|
                                                                                                                                                                                                                                                   
"""

if __name__=='__main__':
    
    ## Declaring an empty list
    ## The list is populated by the function that returns a list
    numList = []
    numList = insertNumbers()

    ## Declaring an empty list to be populated later.
    variants = []

    ## Casting these values to be floats that are returned from the functions
    ## Except for variants which receives a list from getVariants
    meanValue = float(computeMean(numList))
    variants = getVariants(numList, meanValue)
    numVariance = float(computeVariance(variants))
    stdDeviation = float(getStandardDeviation(numVariance))

    ## Finally calling the print results fuction
    printResults(numList, variants, meanValue, numVariance, stdDeviation)

## Assignment: Homework 1
### Names:      Byron Dowling and Israel Olaemimimo
### Class:      Deep Learning
### Semster:    Summer 1 2022
### Date:       6/2/22

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

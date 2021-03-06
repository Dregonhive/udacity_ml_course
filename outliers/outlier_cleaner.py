#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for i in range(len(predictions)):
        cleaned_data.append(tuple([ages[i], net_worths[i], (predictions[i] - net_worths[i])*(predictions[i] - net_worths[i])]))
        print "\n", cleaned_data[i]
    
    cleaned_data.sort(key=lambda x:x[2])
    print "percentage = ", len(cleaned_data)*0.1
    for i in range(10):
        print "\n", cleaned_data[i]
    
    del cleaned_data[len(cleaned_data)-len(cleaned_data)/10:len(cleaned_data)]
    print "-------------------------"
    for i in range(10):
        print "\n", cleaned_data[i]
    print len(cleaned_data)

    return cleaned_data


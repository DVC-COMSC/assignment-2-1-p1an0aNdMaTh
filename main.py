def main():
    def percentage(part, whole):
        percentage = float(part)/float(whole)
        return float(percentage)
    
    m_amount = int(input('Enter the number of male students registered in a class: ')) #ask user for input for number of males
    f_amount = int(input('Enter the number of female students registered in the above class: ')) #ask user for input for number of females

    total_students = int(m_amount) + int(f_amount) #find the total number of students

    
    # m_perc = format(float(percentage(m_amount, total_students)), '.2%') #calculate the percentage of the class that is male
    # f_perc = format(float(percentage(f_amount, total_students)), '.2%') #calculate the percentage of the class that is female
    # m_perc = m_amount / total_students
    # f_perc = f_amount / total_students
    
    print ('The total number of students:', total_students)
    print ('The amount of males:', m_amount)
    print ('The amount of females:', f_amount)
    print ('The percentage of males:', m_perc)
    print ('The percentage of females:', f_perc)
    """
    ##################################################
    Complete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()

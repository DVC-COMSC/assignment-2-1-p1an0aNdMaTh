def main():
    m_amount = input('Enter the number of male students registered in a class.')
    f_amount = input('Enter the number of female students registered in the above class.')
    total_students = int(m_amount) + int(f_amount)
    m_perc = ( int(m_amount) / int(total_students) ) 
    f_perc = ( int(f_amount) / int(total_students) )
    print ('The total number of students:', total_students)
    print ('The amount of females:', m_amount)
    print ('The amount of females:', f_amount)
    print ('The percentage of males:', format (m_perc, '.2%'))
    print ('The percentage of females:', format (f_perc, '.2%'))
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

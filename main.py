def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m_std= int(input('Male students:'))
    f_std= int(input('Female students:'))
    total_std= (m_std + f_std)
    m_perc=(m_std / total_std) *100
    f_perc=(f_std / total_std) *100
    no_males_females=(m_std , f_std)

    print("Total number of students:", total_std)
    print("The number of males and females:", no_males_females)
    print(f'Percentage of males: \t {m_perc:.2f}' + "%")
    print(f'Perecentage of females: \t {f_perc:.2f}' "%")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()

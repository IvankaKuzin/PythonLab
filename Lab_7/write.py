def write_data(row):
    logs = open('data.txt', 'a')
    logs.write( f"{row['CLIENTNUM']} "+ f"{row['Attrition_Flag']} " + f"{row['Customer_Age']} " + f"{row['Gender']} " +
    f"{row['Dependent_count']} "+ f"{row['Education_Level']} " + f"{row['Marital_Status']} " + f"{row['Income_Category']} " +
    f"{row['Card_Category']} " + f"{row['Months_on_book']} "+ f"{row['Total_Relationship_Count']} "+ f"{row['Months_Inactive_12_mon']} "+
    f"{row['Contacts_Count_12_mon']} "+ f"{row['Credit_Limit']} "+ f"{row['Total_Revolving_Bal']} "+ f"{row['Avg_Open_To_Buy']} "+
    f"{row['Total_Amt_Chng_Q4_Q1']} "+ f"{row['Total_Trans_Amt']} "+ f"{row['Total_Trans_Ct']} "+ f"{row['Total_Ct_Chng_Q4_Q1']} "+
    f"{row['Avg_Utilization_Ratio']} "+
    f"{row['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1']} "+
    f"{row['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2']} ")
    logs.write(" \n ")
    logs.close()

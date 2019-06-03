def find_new_salary(current_salary,job_level):
    if job_level==3:
        new_salary=current_salary+current_salary*(15/100)
    elif job_level==4:
        new_salary=current_salary+current_salary*(7/100)
    elif job_level==5:
        new_salary=current_salary+current_salary*(5/100)
    else:
        new_salary=current_salary
    # write your logic here

    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(10000,3)
print(new_salary)

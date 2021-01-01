def my_sum(salary):
    try:
        return salary - (salary * .13)
    except TypeError:
        return



#salary_1 = 55400
salary_1="test"
print(salary_1, my_sum(salary_1))
#print()
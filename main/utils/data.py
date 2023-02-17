variation = ["holofoil", "reverse holo", "1st edition", "1st ed", "1st"]

grading_company = ["psa", "cgc", "bgs", "beckett"]
grades = ['1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5', '5.5', '6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10']

def combine_grade(grading_company, grade):
    combined_list = []
    for company in grading_company:
        for grade in grades:
            combined_list.append(company + " " + grade)
    return combined_list

company_and_grade = combine_grade(grading_company, grades)
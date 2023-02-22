variation = ["holofoil", "reverse holo", "1st edition", "1st ed", "1st"]

grading_company = ["psa", "cgc", "bgs", "beckett"]
grades = ['10', '9.5', '9', '8.5', '8', '7.5', '7', '6.5', '6', '5.5', '5', '4.5', '4', '3.5', '3', '2.5', '2', '1.5', '1']

def combine_grade(grading_company, grade):
    combined_list = []
    for company in grading_company:
        for grade in grades:
            combined_list.append(company + " " + grade)
    return combined_list

company_and_grade = combine_grade(grading_company, grades)
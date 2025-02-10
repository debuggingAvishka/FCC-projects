def arithmetic_arranger(problems, show_answers=True):   
    first_line= []
    second_line= []
    third_line= []
    fourth_line= []

    if len(problems)>5:
        return('Error: Too many problems.')

    for problem in problems:
        parts= problem.split()
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]
        #Error Management
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."
        if int(operand1)>9999 or int(operand2)>9999:
            return('Error: Numbers cannot be more than four digits.')
        if  operator != '+' and operator != '-':
            return("Error: Operator must be '+' or '-'.")

        width = max(len(operand1), len(operand2)) +2

        first_line.append(operand1.rjust(width))
        second_line.append(operator + " " + operand2.rjust(width -2))
        third_line.append('-'* width)
        if show_answers:
            if operator =='+':
                fourth_line.append(str(int(operand1) + int(operand2)).rjust(width))
            elif operator =='-':
                fourth_line.append(str(int(operand1) - int(operand2)).rjust(width))
        
        
#FINAL OUTPUT
    formatted  = "\n".join(["    ".join(first_line),"    ".join(second_line),"    ".join(third_line)])
    if show_answers == True:
        formatted += "\n" + "    ".join(fourth_line)
        
    return formatted       
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
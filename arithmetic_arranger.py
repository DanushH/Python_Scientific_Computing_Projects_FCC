def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ["", "", ""]
    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        arranged_problems[0] += num1.rjust(width) + "    "
        arranged_problems[1] += operator + num2.rjust(width - 1) + "    "
        arranged_problems[2] += "-" * width + "    "

    arranged_problems[0] = arranged_problems[0].rstrip()
    arranged_problems[1] = arranged_problems[1].rstrip()
    arranged_problems[2] = arranged_problems[2].rstrip()
    arranged_problems = "\n".join(arranged_problems)

    if show_answers:
        answers = []
        for problem in problems:
            num1, operator, num2 = problem.split()
            if operator == "+":
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            width = max(len(num1), len(num2)) + 2
            answers.append(result.rjust(width))
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems

# Hey! This tool tells you just how badly you can do and still get your desired grade.

print("Note: Do not convert your percentage scores to decimals (e.g. 94% should be entered as 94)")
psets = float(input("Problem set score: "))
checkpts = float(input("Module checkpoint score: "))
workshts = float(input("Module worksheet score: "))
recitations = float(input("Recitation activity score: "))
quiz_1 = float(input("Quiz 1 score: "))
quiz_2 = float(input("Quiz_2 score: "))
quiz_3 = float(input("Quiz_3 score: "))

final = round((0.3*psets + 0.05*checkpts + 0.1*workshts + 0.06*recitations + 0.12*(quiz_1 + quiz_2 + quiz_3) + (0.13 / 124)*((quiz_1 * 44) + (quiz_2 * 40) + (quiz_3 * 40))), 2)

print("Your final grade is: ", final, '%')

if final < 70.0:
    print("You should take the final exam")
else:
    print("Yay! You will pass without the final exam!")
#enter the score of the candidate
#if score<=50 failed
#if score>=50 and score <=80 just passed
#if score>=80 passed with distinction
score:float= float(input("Enter the score of the candidate: "))
if(score<=50.0):
    print(f'The candidate has scored {score} and has failed')
elif(score>=50.0 and score<=80.0):
    print(f'The candidate has scored {score} and has just passed')
else:
    print(f'The candidate has scored {score} and has passed with distinction')
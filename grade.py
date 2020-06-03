import os as i
b ='\033[92m'
r ='\033[91m'
n ='\033[0m'
def scorequiz(quiz):
   global quizresult
   q = quiz / 160
   score = str(float(q))
   x = score.replace("0.","")
   percent = float(".".join((x[:2],x[2:])))
   result = percent * .30
   quizresult = str(float(result))
def scoreexam(exam):
   global examresult
   q = exam / 60
   score = str(float(q))
   x = score.replace("0.","")
   percent = float(".".join((x[:2],x[2:])))
   result = percent * .20
   examresult = str(float(result))
def scoreperformance(performance):
   global performanceresult
   q = performance / 300
   score = str(float(q))
   x = score.replace("0.","")
   percent = float(".".join((x[:2],x[2:])))
   result = percent * .50
   performanceresult = str(float(result))

if __name__ == "__main__":
   i.system("clear")
   name = input("Your Full Name:"+b)
   quiz = int(input(n+"Your quiz points(30%) over 160:"+b))
   exam = int(input(n+"Your exam points(20%) over 60:"+b))
   performance = int(input(n+"Your performance task points(50%) over 300:"+b))
   scorequiz(quiz)
   scoreexam(exam)
   scoreperformance(performance)
   print(n+"\nYour Quiz Score:"+r+quizresult)
   print(n+"Your Exam Score:"+r+examresult)
   print(n+"Your Performance Score:"+r+performanceresult)
   initialgrade = str(float(quizresult)+float(examresult)+float(performanceresult))
   print(n+"A Total of: "+r+initialgrade)
   print("\n"+b+name+n+"\n\nYour Initial Grade is: "+r+"".join(initialgrade[:5]))

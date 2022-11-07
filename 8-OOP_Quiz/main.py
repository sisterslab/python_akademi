import Classes
import Questions_List as Qlist

quiz_list = Qlist.question_list

quiz = Classes.Quiz(quiz_list)
quiz.showQuestion()
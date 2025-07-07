def run_quiz():
    score=0
    questions=[
        {
            "question":"What is the capital of India?",
            "options":["Delhi","Mumbai","Kolkata","Chennai"],
            "answer":"Delhi"
        },{
           "question":"Which language is used in ML?",
            "options":["Python","Java","C++","PHP"],
            "answer":"Python" 
        }
    ]

    for q in questions:
        print("\n" + q['question'])

        for i,opt in enumerate(q['options']):
            print(f"{i+1}. {opt}")
        choice=int(input("Your Answer (1-4): "))

        if q['options'][choice-1]==q['answer']:
            print("Correct!")
            score+=1
        else:
            print("Wrong Answer")
    print(f"\n Final Score: {score}/{len(questions)}")

run_quiz()
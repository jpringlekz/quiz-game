import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

def input_with_timeout(prompt, timeout):
    # Set the signal handler and a timeout alarm
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    try:
        answer = input(prompt)
        signal.alarm(0)  # Cancel alarm if input given
        return answer
    except TimeoutException:
        print("\nTime's up!")
        return None

def show_progress(current, total):
    bar_length = 20
    progress = int((current / total) * bar_length)
    bar = '#' * progress + '-' * (bar_length - progress)
    print(f"[{bar}] {current}/{total} Questions Answered\n")

def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": {"A": "Paris", "B": "London", "C": "Berlin"},
            "answer": "A"
        },
        {
            "question": "What is 5 + 7?",
            "choices": {"A": "10", "B": "12", "C": "14"},
            "answer": "B"
        },
        {
            "question": "What color do you get when you mix red and white?",
            "choices": {"A": "Pink", "B": "Purple", "C": "Green"},
            "answer": "A"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "choices": {"A": "LeBron James", "B": "William Shakespeare", "C": "Charles Dickens"},
            "answer": "B"
        },
        {
            "question": "What planet is known as the Red Planet?",
            "choices": {"A": "Venus", "B": "Mars", "C": "Jupiter"},
            "answer": "B"
        }
    ]

    score = 0
    total_questions = len(questions)
    time_limit = 10  # seconds per question
    current_question = 0

    print("Welcome to PyTrivia!\n")

    for q in questions:
        current_question += 1
        print(f"{current_question}. {q['question']}")
        for key, value in q['choices'].items():
            print(f"{key}) {value}")
        print(f"(You have {time_limit} seconds to answer)")

        answer = input_with_timeout("Enter A, B, or C: ", time_limit)
        if answer is None:
            print(f"Wrong! The correct answer was {q['answer']}) {q['choices'][q['answer']]}.")
        elif answer.upper() == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}) {q['choices'][q['answer']]}.")
        show_progress(current_question, total_questions)

    print(f"Game Over! Your final score: {score}/{total_questions}")
    if score == total_questions:
        print("Perfect score! You're a trivia master!")
    elif score >= 3:
        print("Great job!")
    else:
        print("Keep practicing!")

if __name__ == "__main__":
    quiz_game()

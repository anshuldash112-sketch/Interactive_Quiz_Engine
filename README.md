Approach Note & Reasoning Checkpoint (B4: Interactive Quiz Engine)
From the PDF guidelines for Track B (Python 3.10+, standard library, console-first) and Problem B4, here is the plan before coding:

Inputs: Case-insensitive single-letter answers (A, B, C, or D) entered interactively in the terminal for each of the 8 questions (with leading/trailing whitespace stripped).

Planned Logic: Store questions, four options each, and the correct answer letter in a list of dictionaries. Loop through each question, prompt the user in a while loop until a valid option (A–D) is entered, provide immediate feedback, update the score, and display the final score and percentage at the end.

Handling Invalid Input (e.g., entering "E"): If the user enters "E" (or any string other than A, B, C, or D), the program rejects it without advancing the question or penalizing the user, prints a clear message listing valid choices (A, B, C, D), and re-prompts for the current question.

Edge Cases Considered:

Entering an out-of-range letter like "E", numbers, empty input/whitespace, or multi-character strings like "AB".

Scoring 0 out of 8 (0.0%) or 8 out of 8 (100.0%), ensuring division is safe and formatting is clean.



SAMPLE RUN
Welcome to the Python Quiz!

Question 1 of 8 : Which built-in data type in Python stores key-value pairs?
  A. list
  B. tuple
  C. dict
  D. set
Enter A, B, C, or D: c
Correct!

Question 2 of 8 : What does the len() function return for 'hello'?
  A. 4
  B. 5
  C. 6
  D. Error
Enter A, B, C, or D: b
Correct!

Question 3 of 8 : Which keyword is used to define a function in Python?
  A. func
  B. function
  C. define
  D. def
Enter A, B, C, or D: d
Correct!

Question 4 of 8 : Which collection is ordered and mutable?
  A. tuple
  B. list
  C. string
  D. int
Enter A, B, C, or D: b
Correct!

Question 5 of 8 : What is the output of bool(0)?
  A. True
  B. False
  C. None
  D. 0
Enter A, B, C, or D: a
Wrong! The right answer was B

Question 6 of 8 : Which operator performs floor division in Python?
  A. /
  B. %
  C. //
  D. **
Enter A, B, C, or D: c
Correct!

Question 7 of 8 : How do you start a comment in Python?
  A. //
  B. /*
  C. #
  D. --
Enter A, B, C, or D: e
Invalid choice! Please type A, B, C, or D.
Enter A, B, C, or D: c
Correct!

Question 8 of 8 : Which method removes and returns the last item of a list by default?
  A. pop()
  B. remove()
  C. discard()
  D. trim()
Enter A, B, C, or D: a
Correct!

Quiz Over!
Your Score: 7 / 8
Percentage: 87.5 %

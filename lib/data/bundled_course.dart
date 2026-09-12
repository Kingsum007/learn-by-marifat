import '../domain/course.dart';

/// Original, bundled course content; no network or first-run download.
class BundledCourse implements CourseRepository {
  @override
  List<Lesson> get lessons => const [
    Lesson(
      id: 'hello',
      title: 'Your first program',
      summary: 'Turn an idea into an instruction.',
      minutes: 8,
      concept:
          'A program is a sequence of instructions. Python runs statements from top to bottom. '
          'The print() function displays a value. Put text inside matching quotes. A line beginning with # is a comment: '
          'it explains the code to a person and is not executed.\n\nTry predicting the output before running each example. '
          'This habit builds your ability to trace a program rather than guess what it does.',
      example: '# A small beginning\nprint("Hello, Afghanistan!")\nprint("I can learn to code.")',
      takeaway: 'Programs run in order. Quotes turn words into string values.',
      exercises: [
        Exercise(
          id: 'hello-q',
          kind: ExerciseKind.choice,
          prompt: 'What does print("Salam") display?',
          options: ['"Salam" including the quotes', 'Salam', 'Nothing'],
          answer: 1,
          explanation: 'Quotes mark the beginning and end of a string. They are not part of the displayed text.',
        ),
        Exercise(
          id: 'hello-o',
          kind: ExerciseKind.order,
          prompt: 'Arrange the lines to display First, then Second.',
          blocks: ['print("First")', 'print("Second")'],
          explanation: 'The first statement runs before the second statement.',
        ),
        Exercise(
          id: 'hello-c',
          kind: ExerciseKind.code,
          prompt: 'Display Salam on one line and Kabul on the next.',
          starter: '# Write two print statements below\n',
          expected: 'Salam\nKabul\n',
          hint: 'Use print("Salam") and then another print statement.',
          explanation: 'Each print() call finishes its output with a new line.',
        ),
      ],
    ),
    Lesson(
      id: 'variables',
      title: 'Names that remember',
      summary: 'Store and update information.',
      minutes: 10,
      concept:
          'A variable gives a name to a value. The assignment operator = evaluates the expression on its right '
          'and stores the result under the name on its left.\n\nIn students = students + 1, Python reads the old '
          'value first, adds one, and then replaces it. This is an update, not a mathematical equation. '
          'Use descriptive names such as student_count. Names are case-sensitive: score and Score are different.',
      example: 'city = "Herat"\nstudents = 24\nstudents = students + 1\nprint(city)\nprint(students)',
      takeaway: 'Assignment stores a value; later assignments can replace it.',
      exercises: [
        Exercise(
          id: 'variables-q',
          kind: ExerciseKind.choice,
          prompt: 'After x = 4 and x = x + 3, what is x?',
          options: ['4', '3', '7'],
          answer: 2,
          explanation:
              'The old value 4 is read, 3 is added, and 7 is stored in x.',
        ),
        Exercise(
          id: 'variables-o',
          kind: ExerciseKind.order,
          prompt: 'Create a score, increase it, then display it.',
          blocks: ['score = 10', 'score = score + 5', 'print(score)'],
          explanation: 'Define a variable before reading it. Print after the update to see the new value.',
        ),
        Exercise(
          id: 'variables-c',
          kind: ExerciseKind.code,
          prompt: 'Create books with value 12, add 3, and print the result.',
          starter: 'books = 12\n# Update books, then print it\n',
          expected: '15\n',
          hint: 'Assign books = books + 3 before print(books).',
          explanation: 'The updated value is 15.',
        ),
      ],
    ),
    Lesson(
      id: 'numbers',
      title: 'Work with numbers',
      summary: 'Calculate, compare, and predict.',
      minutes: 12,
      concept:
          'Use +, -, *, and / for addition, subtraction, multiplication, and division. '
          'Multiplication and division happen before addition and subtraction. Parentheses make the order explicit. '
          '// is floor division and % gives the remainder.\n\nFor 17 books shared among 5 students, '
          '17 // 5 is 3 and 17 % 5 is 2. Each student gets three books and two remain. '
          'Division by zero is an error; check your inputs before dividing.',
      example: 'books = 17\nstudents = 5\nprint(books // students)\nprint(books % students)\nprint((2 + 3) * 4)',
      takeaway:
          'Use parentheses for clarity and remainder for what is left over.',
      exercises: [
        Exercise(
          id: 'numbers-q',
          kind: ExerciseKind.choice,
          prompt: 'What is 2 + 3 * 4?',
          options: ['20', '14', '24'],
          answer: 1,
          explanation: 'Multiply 3 by 4 first, then add 2: the answer is 14.',
        ),
        Exercise(
          id: 'numbers-o',
          kind: ExerciseKind.order,
          prompt: 'Calculate the total cost of five notebooks at 20 each.',
          blocks: ['price = 20', 'total = price * 5', 'print(total)'],
          explanation:
              'The unit price must be defined before calculating the total.',
        ),
        Exercise(
          id: 'numbers-c',
          kind: ExerciseKind.code,
          prompt: 'Print the remainder when 23 is divided by 4.',
          starter: '# Use the remainder operator\n',
          expected: '3\n',
          hint: 'The % operator computes a remainder.',
          explanation: '4 fits into 23 five times, leaving 3.',
        ),
      ],
    ),
    Lesson(
      id: 'decisions',
      title: 'Make a decision',
      summary: 'Let conditions choose the next step.',
      minutes: 12,
      concept:
          'An if statement runs an indented block only when its condition is true. '
          'An optional else block handles the other case. End each if or else header with a colon and indent '
          'the block by four spaces.\n\nUse == to compare equality, != for inequality, and <, <=, >, >= '
          'for ordering. The operator = assigns; == compares. Boolean values are True and False. '
          'Use and, or, and not to combine or invert conditions.',
      example: 'score = 72\nif score >= 50:\n    print("Pass")\nelse:\n    print("Keep practicing")',
      takeaway:
          'A condition chooses a branch; indentation defines the branch body.',
      exercises: [
        Exercise(
          id: 'decisions-q',
          kind: ExerciseKind.choice,
          prompt: 'Which expression checks whether score equals 50?',
          options: ['score = 50', 'score == 50', 'score + 50'],
          answer: 1,
          explanation: '== compares two values. A single = is an assignment.',
        ),
        Exercise(
          id: 'decisions-o',
          kind: ExerciseKind.order,
          prompt: 'Set a temperature and print Cold when it is below 10.',
          blocks: [
            'temperature = 5',
            'if temperature < 10:',
            '    print("Cold")',
          ],
          explanation: 'Define the value, test it, and indent the action under the condition.',
        ),
        Exercise(
          id: 'decisions-c',
          kind: ExerciseKind.code,
          prompt: 'Complete this condition so the program displays Pass.',
          starter: 'score = 65\n# Write an if statement that prints Pass when score >= 50\n',
          expected: 'Pass\n',
          hint: 'Use if score >= 50: followed by an indented print("Pass").',
          explanation:
              '65 meets the condition score >= 50, so the indented print runs.',
        ),
      ],
    ),
    Lesson(
      id: 'loops',
      title: 'Repeat with purpose',
      summary: 'Use loops to do the repetitive work.',
      minutes: 14,
      concept:
          'A for loop visits each value in a sequence. range(1, 4) produces 1, 2, and 3: '
          'the end is excluded. range(4) starts at zero.\n\nAn accumulator starts with an initial value '
          'and is updated on each iteration. For a sum, start at zero. Put the final print outside the loop '
          'when you want just the total.\n\nA while loop repeats while a condition is true. '
          'Update the controlling variable so the loop can finish. The practice runner stops excessive execution.',
      example: 'total = 0\nfor number in range(1, 5):\n    total = total + number\nprint(total)',
      takeaway:
          'range excludes its stop value. Indentation controls what repeats.',
      exercises: [
        Exercise(
          id: 'loops-q',
          kind: ExerciseKind.choice,
          prompt: 'Which values does range(1, 4) produce?',
          options: ['1, 2, 3, 4', '0, 1, 2, 3', '1, 2, 3'],
          answer: 2,
          explanation: 'The start is included and the stop is excluded.',
        ),
        Exercise(
          id: 'loops-o',
          kind: ExerciseKind.order,
          prompt: 'Accumulate 1 + 2 + 3 and display the final sum.',
          blocks: [
            'total = 0',
            'for n in range(1, 4):',
            '    total = total + n',
            'print(total)',
          ],
          explanation:
              'Initialize once, update inside the loop, then print outside it.',
        ),
        Exercise(
          id: 'loops-c',
          kind: ExerciseKind.code,
          prompt: 'Use a loop to print 1, 2, and 3 on separate lines.',
          starter: '# A for loop with range\n',
          expected: '1\n2\n3\n',
          hint: 'Use for n in range(1, 4): and indent print(n).',
          explanation: 'The three iterations bind n to 1, 2, and then 3.',
        ),
      ],
    ),
    Lesson(
      id: 'lists',
      title: 'Keep things together',
      summary: 'Organize a collection of values.',
      minutes: 12,
      concept:
          'A list stores a sequence of values between square brackets. Indexing starts at zero, '
          'so cities[0] retrieves the first item. len(cities) gives the number of items. '
          'An index outside the list raises an error.\n\nA for loop can visit list values directly: '
          'for city in cities. This is useful when you need each value without its position. '
          'The practice runner supports list literals, reading indexes, len(), and iteration; '
          'list methods and index assignment are outside this version.',
      example: 'cities = ["Kabul", "Bamyan", "Herat"]\nprint(cities[0])\nprint(len(cities))\nfor city in cities:\n    print(city)',
      takeaway: 'Lists group values. The first item has index zero.',
      exercises: [
        Exercise(
          id: 'lists-q',
          kind: ExerciseKind.choice,
          prompt: 'For marks = [70, 80, 90], what is marks[1]?',
          options: ['70', '80', '90'],
          answer: 1,
          explanation: 'Index 0 is 70, index 1 is 80, and index 2 is 90.',
        ),
        Exercise(
          id: 'lists-o',
          kind: ExerciseKind.order,
          prompt: 'Store names, loop over them, and display each name.',
          blocks: [
            'names = ["Amina", "Omid"]',
            'for name in names:',
            '    print(name)',
          ],
          explanation:
              'The loop visits each name and the indented print displays it.',
        ),
        Exercise(
          id: 'lists-c',
          kind: ExerciseKind.code,
          prompt: 'Print the sum of all three marks using an accumulator.',
          starter: 'marks = [10, 20, 30]\ntotal = 0\n# Loop through marks, then print total\n',
          expected: '60\n',
          hint: 'Add each mark to total inside a for loop. Print total after the loop.',
          explanation:
              'Starting at zero, the running total becomes 10, 30, then 60.',
        ),
      ],
    ),
    Lesson(
      id: 'functions',
      title: 'Build reusable ideas',
      summary: 'Name a process and use it again.',
      minutes: 14,
      concept:
          'A function packages instructions under a name. Define it with def, a name, parentheses, '
          'and a colon. Parameters are names for values supplied by the caller. return sends a result '
          'back and ends the function.\n\nA returned value is not automatically displayed: use print() '
          'to display it. Variables assigned inside these simple functions belong to that function call. '
          'Start with small functions that each do one clear thing.',
      example: 'def square(number):\n    return number * number\n\nprint(square(4))\nprint(square(7))',
      takeaway: 'Parameters carry values in; return carries a result out.',
      exercises: [
        Exercise(
          id: 'functions-q',
          kind: ExerciseKind.choice,
          prompt: 'What does return do inside a function?',
          options: [
            'Always prints text',
            'Sends a value to the caller and exits',
            'Repeats the function',
          ],
          answer: 1,
          explanation: 'return exits the function with a value. print() is a separate operation.',
        ),
        Exercise(
          id: 'functions-o',
          kind: ExerciseKind.order,
          prompt: 'Define a function that doubles a number, then use it.',
          blocks: ['def double(n):', '    return n * 2', 'print(double(5))'],
          explanation: 'Define the function before calling it. Its return statement is indented.',
        ),
        Exercise(
          id: 'functions-c',
          kind: ExerciseKind.code,
          prompt: 'Define add(a, b) and print add(4, 6).',
          starter: '# Define add, return a + b, then print a call\n',
          expected: '10\n',
          hint: 'Use def add(a, b): with an indented return a + b.',
          explanation:
              'The arguments 4 and 6 become a and b; the function returns 10.',
        ),
      ],
    ),
  ];
}

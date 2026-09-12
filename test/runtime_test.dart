import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/runtime/code_runner.dart';
import 'package:learn_by_marifat_team/runtime/python_vm.dart';

void main() {
  final vm = PythonVm();
  final programs = <String, String>{
    'print("Salam")': 'Salam\n',
    'x = 4\nx = x + 3\nprint(x)': '7\n',
    'print(2 + 3 * 4)\nprint((2 + 3) * 4)': '14\n20\n',
    'print(-7 // 3)\nprint(-7 % 3)\nprint(7 % -3)': '-3\n2\n-2\n',
    'if 1 > 2:\n    print("No")\nelse:\n    print("Yes")': 'Yes\n',
    'total = 0\nfor n in range(1, 5):\n    total = total + n\nprint(total)':
        '10\n',
    'i = 0\nwhile i < 3:\n    print(i)\n    i = i + 1': '0\n1\n2\n',
    'print([70, 80, 90][1])\nprint([1, 2][-1])': '80\n2\n',
    'def add(a, b):\n    return a + b\nprint(add(4, 6))': '10\n',
    'def fact(n):\n    if n <= 1:\n        return 1\n    return n * fact(n - 1)\nprint(fact(5))':
        '120\n',
    'print(False and missing)\nprint(True or missing)\nprint(not 3 == 4)':
        'False\nTrue\nTrue\n',
    'for n in range(3, 0, -1):\n    print(n)': '3\n2\n1\n',
    'print(len([1, 2]))\nprint(int("5") + 1)\nprint(str(5) + " books")':
        '2\n6\n5 books\n',
    '# comment\nprint("# is text") # comment': '# is text\n',
    'print("سلام")': 'سلام\n',
  };
  for (final entry in programs.entries) {
    test('executes ${entry.key.split('\n').first}', () {
      final result = vm.run(entry.key);
      expect(result.error, isNull, reason: result.error);
      expect(result.output, entry.value);
    });
  }
  for (final lesson in BundledCourse().lessons) {
    test(
      'bundled ${lesson.id} example executes',
      () => expect(vm.run(lesson.example).error, isNull),
    );
    test(
      'bundled ${lesson.id} ordering solution executes',
      () => expect(vm.run(lesson.exercises[1].blocks.join('\n')).error, isNull),
    );
  }
  final failures = <String, String>{
    'print(1 / 0)': 'divide by zero',
    'print(missing)': 'not defined',
    'if True:\n  print(1)': 'four spaces',
    'print([1][9])': 'outside',
    'while True:\n    pass': 'Execution limit',
    'print(range(100000000))': '1,000',
    'print("x" * 1000000000)': 'limit',
    'def f():\n    return f()\nf()': 'depth limit',
    'import os': 'Expected a value',
    'open("secret")': 'unavailable',
    'print(1 < 2 < 3)': 'and between',
    'for n in range(1000):\n    print("x" * 100)': 'Output limit',
    'x = [1]\nfor n in range(30):\n    x = [x, x]\nprint(x)': 'Nested value',
    'print("unclosed)': 'matching quote',
    'return 1': 'inside a function',
  };
  for (final entry in failures.entries) {
    test(
      'rejects safely ${entry.key.split('\n').first}',
      () => expect(vm.run(entry.key).error, contains(entry.value)),
    );
  }
  test('each run starts clean', () {
    vm.run('x = 5');
    expect(vm.run('print(x)').error, contains('not defined'));
  });
  test('worker returns bounded result', () async {
    final result = await IsolateCodeRunner().run('print(42)');
    expect(result.output, '42\n');
  });
}

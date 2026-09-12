import 'dart:math' as math;

class RunResult {
  const RunResult(this.output, {this.error, this.steps = 0});
  final String output;
  final String? error;
  final int steps;
  bool get succeeded => error == null;
}

/// A deliberately small teaching interpreter, NOT CPython. It never executes
/// host code. Values are numbers, strings, booleans, null and bounded lists.
class PythonVm {
  RunResult run(String source) {
    final context = _Context();
    try {
      if (source.length > 12000) {
        throw _Fault('Programs are limited to 12,000 characters.');
      }
      final lines = <_Line>[];
      var number = 0;
      for (final raw in source.replaceAll('\r\n', '\n').split('\n')) {
        number++;
        if (raw.contains('\t')) {
          throw _Fault('Use four spaces instead of tabs.', number);
        }
        if (raw.trim().isEmpty || raw.trimLeft().startsWith('#')) {
          continue;
        }
        final indent = raw.length - raw.trimLeft().length;
        if (indent % 4 != 0) {
          throw _Fault('Indentation must use groups of four spaces.', number);
        }
        lines.add(_Line(indent, raw.trim(), number));
      }
      final parser = _ProgramParser(lines);
      final statements = parser.block(0);
      if (parser.position != lines.length) {
        throw _Fault('Unexpected indentation.', lines[parser.position].number);
      }
      _execute(statements, context, <String, Object?>{});
      return RunResult(context.output.toString(), steps: context.steps);
    } on _Fault catch (e) {
      return RunResult(
        context.output.toString(),
        error: e.toString(),
        steps: context.steps,
      );
    } on _Return {
      return RunResult(
        context.output.toString(),
        error: 'return must be inside a function.',
        steps: context.steps,
      );
    } catch (_) {
      return RunResult(
        context.output.toString(),
        error: 'Unsupported operation. Check the language guide.',
        steps: context.steps,
      );
    }
  }
}

class _Fault implements Exception {
  _Fault(this.message, [this.line]);
  final String message;
  final int? line;
  @override
  String toString() => line == null ? message : 'Line $line: $message';
}

class _Context {
  final output = StringBuffer();
  final functions = <String, _Statement>{};
  Map<String, Object?> globals = {};
  int steps = 0, depth = 0;
  void tick() {
    if (++steps > 20000) {
      throw _Fault('Execution limit reached. Check your loop condition.');
    }
  }

  void printValues(List<Object?> values) {
    final text = '${values.map(_display).join(' ')}\n';
    if (output.length + text.length > 16000) {
      throw _Fault('Output limit reached (16,000 characters).');
    }
    output.write(text);
  }
}

String _display(Object? value) {
  if (value == null) {
    return 'None';
  }
  if (value is bool) {
    return value ? 'True' : 'False';
  }
  if (value is List) {
    return '[${value.map((v) => v is String ? "'$v'" : _display(v)).join(', ')}]';
  }
  return value.toString();
}

bool _truth(Object? value) =>
    value != null &&
    value != false &&
    value != 0 &&
    value != '' &&
    !(value is List && value.isEmpty);
num _number(Object? value) {
  if (value is num) {
    return value;
  }
  if (value is bool) {
    return value ? 1 : 0;
  }
  throw _Fault('This operation needs a number.');
}

Object? _bounded(Object? value) {
  var units = 0;
  void measure(Object? item, int depth) {
    units += item is String ? item.length + 2 : 1;
    if (depth > 32 || units > 12000) {
      throw _Fault('Nested value exceeds the practice limit.');
    }
    if (item is List) {
      for (final child in item) {
        measure(child, depth + 1);
      }
    }
  }

  measure(value, 0);
  if (value is String && value.length > 12000 ||
      value is List && value.length > 1000) {
    throw _Fault('Value is too large for the practice runner.');
  }
  if (value is num && (!value.isFinite || value.abs() > 1e15)) {
    throw _Fault('Number exceeds the practice limit.');
  }
  return value;
}

class _Line {
  _Line(this.indent, this.text, this.number);
  final int indent, number;
  final String text;
}

class _Statement {
  _Statement(
    this.kind,
    this.line, {
    this.name = '',
    this.expression,
    this.body = const [],
    this.otherwise = const [],
    this.parameters = const [],
  });
  final String kind, name;
  final int line;
  final _Expression? expression;
  final List<_Statement> body, otherwise;
  final List<String> parameters;
}

class _ProgramParser {
  _ProgramParser(this.lines);
  final List<_Line> lines;
  int position = 0;
  List<_Statement> block(int indent) {
    if (indent > 128) {
      throw _Fault('Nesting limit reached.');
    }
    final result = <_Statement>[];
    while (position < lines.length && lines[position].indent >= indent) {
      final line = lines[position];
      if (line.indent != indent) {
        throw _Fault('Unexpected indentation.', line.number);
      }
      if (line.text == 'else:') {
        break;
      }
      position++;
      try {
        result.add(statement(line));
      } on _Fault catch (e) {
        throw _Fault(e.message, e.line ?? line.number);
      }
    }
    return result;
  }

  List<_Statement> body(_Line parent) {
    if (position >= lines.length ||
        lines[position].indent != parent.indent + 4) {
      throw _Fault('Expected an indented block.', parent.number);
    }
    return block(parent.indent + 4);
  }

  _Statement statement(_Line line) {
    final text = line.text;
    for (final kind in ['if', 'while']) {
      if (text.startsWith('$kind ')) {
        if (!text.endsWith(':')) {
          throw _Fault('Add a colon after the condition.');
        }
        final expression = _parse(
          text.substring(kind.length + 1, text.length - 1),
        );
        final children = body(line);
        var otherwise = <_Statement>[];
        if (kind == 'if' &&
            position < lines.length &&
            lines[position].indent == line.indent &&
            lines[position].text == 'else:') {
          final other = lines[position++];
          otherwise = body(other);
        }
        return _Statement(
          kind,
          line.number,
          expression: expression,
          body: children,
          otherwise: otherwise,
        );
      }
    }
    final loop = RegExp(r'^for ([a-zA-Z_]\w*) in (.+):$').firstMatch(text);
    if (loop != null) {
      final expression = _parse(loop[2]!);
      return _Statement(
        'for',
        line.number,
        name: loop[1]!,
        expression: expression,
        body: body(line),
      );
    }
    final function = RegExp(r'^def ([a-zA-Z_]\w*)\(([^)]*)\):$')
        .firstMatch(text);
    if (function != null) {
      final parameters = function[2]!.trim().isEmpty
          ? <String>[]
          : function[2]!.split(',').map((s) => s.trim()).toList();
      if (parameters.length > 10 ||
          parameters.toSet().length != parameters.length ||
          parameters.any((s) => !RegExp(r'^[a-zA-Z_]\w*$').hasMatch(s))) {
        throw _Fault('Use unique, simple parameter names.');
      }
      return _Statement(
        'def',
        line.number,
        name: function[1]!,
        parameters: parameters,
        body: body(line),
      );
    }
    if (text == 'return' || text.startsWith('return ')) {
      return _Statement(
        'return',
        line.number,
        expression: text == 'return'
            ? _Literal(null)
            : _parse(text.substring(7)),
      );
    }
    if (text == 'pass') {
      return _Statement('pass', line.number);
    }
    final assignment = RegExp(r'^([a-zA-Z_]\w*)\s*=(?!=)\s*(.+)$')
        .firstMatch(text);
    if (assignment != null) {
      return _Statement(
        'assign',
        line.number,
        name: assignment[1]!,
        expression: _parse(assignment[2]!),
      );
    }
    return _Statement('expression', line.number, expression: _parse(text));
  }
}

void _execute(
  List<_Statement> statements,
  _Context context,
  Map<String, Object?> scope,
) {
  if (context.depth == 0) {
    context.globals = scope;
  }
  for (final statement in statements) {
    context.tick();
    try {
      Object? value() => statement.expression!.evaluate(context, scope);
      switch (statement.kind) {
        case 'assign':
          scope[statement.name] = value();
        case 'expression':
          value();
        case 'if':
          _execute(
            _truth(value()) ? statement.body : statement.otherwise,
            context,
            scope,
          );
        case 'while':
          while (_truth(value())) {
            context.tick();
            _execute(statement.body, context, scope);
          }
        case 'for':
          final iterable = value();
          final Iterable<Object?> items;
          if (iterable is List) {
            items = iterable;
          } else if (iterable is String) {
            items = iterable.split('');
          } else {
            throw _Fault('A for loop needs a list, string, or range.');
          }
          for (final item in items) {
            context.tick();
            scope[statement.name] = item;
            _execute(statement.body, context, scope);
          }
        case 'def':
          if (context.depth != 0) {
            throw _Fault('Nested functions are outside this runner.');
          }
          context.functions[statement.name] = statement;
        case 'return':
          throw _Return(value());
        case 'pass':
          break;
      }
    } on _Fault catch (e) {
      throw _Fault(e.message, e.line ?? statement.line);
    }
  }
}

class _Return implements Exception {
  _Return(this.value);
  final Object? value;
}

abstract class _Expression {
  Object? evaluate(_Context context, Map<String, Object?> scope);
}

class _Literal extends _Expression {
  _Literal(this.value);
  final Object? value;
  @override
  Object? evaluate(_Context context, Map<String, Object?> scope) {
    context.tick();
    return value;
  }
}

class _Name extends _Expression {
  _Name(this.name);
  final String name;
  @override
  Object? evaluate(_Context context, Map<String, Object?> scope) {
    context.tick();
    if (!scope.containsKey(name)) {
      throw _Fault('Name "$name" is not defined.');
    }
    return scope[name];
  }
}

class _Sequence extends _Expression {
  _Sequence(this.items);
  final List<_Expression> items;
  @override
  Object? evaluate(_Context context, Map<String, Object?> scope) =>
      _bounded(items.map((e) => e.evaluate(context, scope)).toList());
}

class _Index extends _Expression {
  _Index(this.target, this.index);
  final _Expression target, index;
  @override
  Object? evaluate(_Context context, Map<String, Object?> scope) {
    final value = target.evaluate(context, scope),
        i = index.evaluate(context, scope);
    if (i is! int || (value is! List && value is! String)) {
      throw _Fault('Index a list or string with an integer.');
    }
    final length = value is List ? value.length : (value as String).length;
    final offset = i < 0 ? length + i : i;
    if (offset < 0 || offset >= length) {
      throw _Fault('Index is outside the sequence.');
    }
    return value is List ? value[offset] : (value as String)[offset];
  }
}

class _Unary extends _Expression {
  _Unary(this.operator, this.expression);
  final String operator;
  final _Expression expression;
  @override
  Object? evaluate(_Context context, Map<String, Object?> scope) {
    final value = expression.evaluate(context, scope);
    return switch (operator) {
      'not' => !_truth(value),
      '-' => -_number(value),
      _ => _number(value),
    };
  }
}

class _Binary extends _Expression {
  _Binary(this.operator, this.left, this.right);
  final String operator;
  final _Expression left, right;
  @override
  Object? evaluate(_Context context, Map<String, Object?> scope) {
    context.tick();
    final a = left.evaluate(context, scope);
    if (operator == 'and') {
      return _truth(a) ? right.evaluate(context, scope) : a;
    }
    if (operator == 'or') {
      return _truth(a) ? a : right.evaluate(context, scope);
    }
    final b = right.evaluate(context, scope);
    if (operator == '==' || operator == '!=') {
      bool equal(Object? x, Object? y) => x is List && y is List
          ? x.length == y.length &&
                List.generate(
                  x.length,
                  (i) => equal(x[i], y[i]),
                ).every((v) => v)
          : x == y;
      return operator == '==' ? equal(a, b) : !equal(a, b);
    }
    if (operator == '+' && a is String && b is String) {
      return _bounded(a + b);
    }
    if (operator == '+' && a is List && b is List) {
      return _bounded([...a, ...b]);
    }
    if (operator == '*' &&
        ((a is String && b is int) || (a is int && b is String))) {
      final string = (a is String ? a : b) as String,
          count = (a is int ? a : b) as int;
      if (string.length * math.max(0, count) > 12000 || count > 12000) {
        throw _Fault('String repetition exceeds the limit.');
      }
      return string * math.max(0, count);
    }
    final x = _number(a), y = _number(b);
    if (['/', '//', '%'].contains(operator) && y == 0) {
      throw _Fault('Cannot divide by zero.');
    }
    return _bounded(switch (operator) {
      '+' => x + y,
      '-' => x - y,
      '*' => x * y,
      '/' => x / y,
      '//' => (x / y).floor(),
      '%' => x - (x / y).floor() * y,
      '<' => x < y,
      '<=' => x <= y,
      '>' => x > y,
      '>=' => x >= y,
      _ => throw _Fault('Unsupported operator $operator.'),
    });
  }
}

class _Call extends _Expression {
  _Call(this.name, this.arguments);
  final String name;
  final List<_Expression> arguments;
  @override
  Object? evaluate(_Context context, Map<String, Object?> scope) {
    context.tick();
    final args = arguments.map((e) => e.evaluate(context, scope)).toList();
    void count(int n) {
      if (args.length != n) {
        throw _Fault('$name needs $n argument(s).');
      }
    }

    switch (name) {
      case 'print':
        context.printValues(args);
        return null;
      case 'len':
        count(1);
        final value = args.first;
        if (value is List) {
          return value.length;
        }
        if (value is String) {
          return value.length;
        }
        throw _Fault('len needs a list or string.');
      case 'str':
        count(1);
        return _bounded(_display(args.first));
      case 'int':
        count(1);
        final value = args.first;
        if (value is num) {
          return value.toInt();
        }
        if (value is bool) {
          return value ? 1 : 0;
        }
        final parsed = int.tryParse(value.toString());
        if (parsed == null) {
          throw _Fault('Cannot convert this value to an integer.');
        }
        return _bounded(parsed);
      case 'range':
        if (args.isEmpty || args.length > 3 || args.any((a) => a is! int)) {
          throw _Fault('range needs 1 to 3 integers.');
        }
        final start = args.length == 1 ? 0 : args[0] as int;
        final stop = args.length == 1 ? args[0] as int : args[1] as int;
        final step = args.length == 3 ? args[2] as int : 1;
        if (step == 0) {
          throw _Fault('range step cannot be zero.');
        }
        final length = math.max(0, ((stop - start) / step).ceil());
        if (length > 1000) {
          throw _Fault('range is limited to 1,000 items.');
        }
        return List.generate(length, (i) => start + i * step);
    }
    final function = context.functions[name];
    if (function == null) {
      throw _Fault('Function "$name" is unavailable. See the language guide.');
    }
    count(function.parameters.length);
    if (++context.depth > 32) {
      throw _Fault('Function call depth limit reached.');
    }
    final local = Map<String, Object?>.of(context.globals);
    for (var i = 0; i < args.length; i++) {
      local[function.parameters[i]] = args[i];
    }
    try {
      _execute(function.body, context, local);
    } on _Return catch (result) {
      return result.value;
    } finally {
      context.depth--;
    }
    return null;
  }
}

class _Token {
  _Token(this.text, {this.literal, this.isLiteral = false});
  final String text;
  final Object? literal;
  final bool isLiteral;
}

List<_Token> _lex(String source) {
  final tokens = <_Token>[];
  var i = 0;
  while (i < source.length) {
    final char = source[i];
    if (char.trim().isEmpty) {
      i++;
      continue;
    }
    if (char == '#') {
      break;
    }
    if (char == '"' || char == "'") {
      final quote = char, value = StringBuffer();
      i++;
      while (i < source.length && source[i] != quote) {
        if (source[i] == r'\') {
          i++;
          if (i == source.length) {
            throw _Fault('Unfinished string escape.');
          }
          value.write(switch (source[i]) {
            'n' => '\n',
            't' => '\t',
            'r' => '\r',
            '\\' => '\\',
            '"' => '"',
            "'" => "'",
            _ => throw _Fault('Unsupported string escape.'),
          });
          i++;
        } else {
          value.write(source[i++]);
        }
      }
      if (i == source.length) {
        throw _Fault('Close the string with a matching quote.');
      }
      i++;
      tokens.add(_Token('string', literal: value.toString(), isLiteral: true));
      continue;
    }
    final rest = source.substring(i);
    final number = RegExp(r'^\d+(\.\d+)?').firstMatch(rest);
    if (number != null) {
      final text = number[0]!;
      tokens.add(
        _Token(text, literal: _bounded(num.parse(text)), isLiteral: true),
      );
      i += text.length;
      continue;
    }
    final name = RegExp(r'^[a-zA-Z_]\w*').firstMatch(rest);
    if (name != null) {
      final text = name[0]!;
      tokens.add(switch (text) {
        'True' => _Token(text, literal: true, isLiteral: true),
        'False' => _Token(text, literal: false, isLiteral: true),
        'None' => _Token(text, isLiteral: true),
        _ => _Token(text),
      });
      i += text.length;
      continue;
    }
    if (i + 1 < source.length &&
        ['==', '!=', '<=', '>=', '//'].contains(source.substring(i, i + 2))) {
      tokens.add(_Token(source.substring(i, i + 2)));
      i += 2;
      continue;
    }
    if ('+-*/%<>()[],'.contains(char)) {
      tokens.add(_Token(char));
      i++;
      continue;
    }
    throw _Fault('Unsupported character "$char". See the language guide.');
  }
  tokens.add(_Token('<end>'));
  return tokens;
}

_Expression _parse(String source) {
  final parser = _ExpressionParser(_lex(source));
  final result = parser.expression();
  if (parser.current.text != '<end>') {
    throw _Fault('Unexpected "${parser.current.text}".');
  }
  return result;
}

class _ExpressionParser {
  _ExpressionParser(this.tokens);
  final List<_Token> tokens;
  int position = 0, depth = 0;
  _Token get current => tokens[position];
  bool accept(String text) {
    if (current.text == text) {
      position++;
      return true;
    }
    return false;
  }

  void expect(String text) {
    if (!accept(text)) {
      throw _Fault('Expected "$text".');
    }
  }

  static const precedence = {
    'or': 1,
    'and': 2,
    '==': 3,
    '!=': 3,
    '<': 3,
    '>': 3,
    '<=': 3,
    '>=': 3,
    '+': 4,
    '-': 4,
    '*': 5,
    '/': 5,
    '//': 5,
    '%': 5,
  };
  _Expression expression([int minimum = 0]) {
    if (++depth > 64) {
      throw _Fault('Expression nesting limit reached.');
    }
    var left = primary();
    var comparisonSeen = false;
    while (precedence.containsKey(current.text) &&
        precedence[current.text]! >= minimum) {
      final op = current.text, priority = precedence[op]!;
      if (priority == 3 && comparisonSeen) {
        throw _Fault('Use and between comparisons in this runner.');
      }
      if (priority == 3) {
        comparisonSeen = true;
      }
      position++;
      left = _Binary(op, left, expression(priority + 1));
    }
    depth--;
    return left;
  }

  _Expression primary() {
    _Expression result;
    final token = current;
    if (accept('not')) {
      return _Unary('not', expression(3));
    }
    if (accept('-')) {
      return _Unary('-', expression(6));
    }
    if (accept('+')) {
      return _Unary('+', expression(6));
    }
    if (token.isLiteral) {
      position++;
      result = _Literal(token.literal);
    } else if (accept('(')) {
      result = expression();
      expect(')');
    } else if (accept('[')) {
      final items = <_Expression>[];
      if (!accept(']')) {
        do {
          items.add(expression());
        } while (accept(','));
        expect(']');
      }
      result = _Sequence(items);
    } else if (RegExp(r'^[a-zA-Z_]\w*$').hasMatch(token.text) &&
        ![
          'and',
          'or',
          'import',
          'while',
          'for',
          'if',
          'def',
          'else',
          'class',
        ].contains(token.text)) {
      position++;
      if (accept('(')) {
        final arguments = <_Expression>[];
        if (!accept(')')) {
          do {
            arguments.add(expression());
          } while (accept(','));
          expect(')');
        }
        result = _Call(token.text, arguments);
      } else {
        result = _Name(token.text);
      }
    } else {
      throw _Fault('Expected a value, found "${token.text}".');
    }
    while (accept('[')) {
      result = _Index(result, expression());
      expect(']');
    }
    return result;
  }
}

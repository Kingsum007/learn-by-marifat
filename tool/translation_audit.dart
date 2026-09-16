import 'dart:convert';
import 'dart:io';

import 'package:analyzer/dart/analysis/utilities.dart';
import 'package:analyzer/dart/ast/ast.dart';
import 'package:analyzer/dart/ast/visitor.dart';

/// Extract literals and interpolation templates from the actual Dart AST.
/// The explicit exclusions below are code, IDs, filenames or font identifiers.
class InventoryVisitor extends RecursiveAstVisitor<void> {
  final Set<String> inventory = {};
  void collect(StringLiteral node) {
    if (node.parent is AdjacentStrings) return;
    var n = 0;
    String render(StringLiteral node) {
      if (node is SimpleStringLiteral) return node.value;
      if (node is AdjacentStrings) return node.strings.map(render).join();
      if (node is StringInterpolation) {
        return node.elements
            .map((e) => e is InterpolationString ? e.value : '{${n++}}')
            .join();
      }
      return '';
    }

    final value = render(node);
    if (!RegExp('[a-zA-Z]{2}').hasMatch(value)) return;
    if (value.startsWith('package:') ||
        value.startsWith('../') ||
        value.endsWith('.dart')) {
      return;
    }
    if ({
      'LearnSans',
      'LearnMono',
      'monospace',
      'en',
      'fa',
      'ps',
      'playground',
      'lab-language',
      'python',
      'database-foundations',
      'sql',
      'sqlite',
      'trace',
      'practice',
      'review',
      'run-code',
      'code-editor',
      'save-portfolio',
      'evidence',
      'milestones',
      'scores',
      'format',
      'version',
      'solved',
      'bookmarks',
      'drafts',
      'attempts',
      'language',
      'dark',
      'portfolio',
      'kohi-backup',
    }.contains(value)) {
      return;
    }
    if (value.contains('name = "Afghanistan"') ||
        value.contains('CREATE TABLE') ||
        value.startsWith('org.')) {
      return;
    }
    // Only human-readable error messages from runtime and state files are used.
    if ({
      '.py',
      'App.jsx',
      'LearnArabic',
      'Main.kt',
      'NOTES.md',
      'README.md',
      'TESTS.md',
      'android',
      'cpp',
      'flutter-dart',
      'index.html',
      'ios',
      'java',
      'kotlin',
      'main.cpp',
      'main.js',
      'main.swift',
      'reactjs',
      'reactnative',
      'save-workspace',
      'swift',
      'web-design',
      'workspace-editor',
    }.contains(value)) {
      return;
    }
    if ({
      'assets/brand/marifat.png',
      'cancel',
      'discard',
      'save',
    }.contains(value)) {
      return;
    }
    inventory.add(value);
  }

  @override
  void visitSimpleStringLiteral(SimpleStringLiteral node) {
    collect(node);
    super.visitSimpleStringLiteral(node);
  }

  @override
  void visitStringInterpolation(StringInterpolation node) {
    collect(node);
    super.visitStringInterpolation(node);
  }

  @override
  void visitAdjacentStrings(AdjacentStrings node) {
    collect(node);
    super.visitAdjacentStrings(node);
  }
}

void main() {
  final visitor = InventoryVisitor();
  for (final file
      in Directory('lib/presentation').listSync().whereType<File>().where(
        (f) =>
            f.path.endsWith('.dart') &&
            !f.path.endsWith('localized_text.dart') &&
            !f.path.endsWith('learning_localizations.dart'),
      )) {
    parseString(content: file.readAsStringSync()).unit.accept(visitor);
  }
  for (final file in [
    'lib/runtime/code_runner.dart',
    'lib/runtime/python_vm.dart',
    'lib/runtime/sql_practice.dart',
    'lib/domain/learner_state.dart',
    'lib/domain/portfolio.dart',
    'lib/application/learning_controller.dart',
  ]) {
    final source = File(file).readAsStringSync();
    // Runtime code has many language-token literals; only exception arguments
    // and the two RunResult error messages are instructional prose.
    final parsed = parseString(content: source).unit;
    parsed.accept(_Errors(visitor));
  }
  final output = visitor.inventory.toList()..sort();
  File('assets/curriculum/ui_inventory.json')
      .writeAsStringSync(const JsonEncoder.withIndent('  ').convert(output));
  stdout.writeln('Inventoried ${output.length} authored UI/error messages.');
}

class _Errors extends RecursiveAstVisitor<void> {
  _Errors(this.target);
  final InventoryVisitor target;
  @override
  void visitInstanceCreationExpression(InstanceCreationExpression node) {
    if ([
      '_Fault',
      'FormatException',
    ].contains(node.constructorName.type.name.lexeme)) {
      for (final argument in node.argumentList.arguments) {
        if (argument is StringLiteral) target.collect(argument);
      }
    }
    super.visitInstanceCreationExpression(node);
  }

  @override
  void visitNamedExpression(NamedExpression node) {
    if (node.name.label.name == 'error' && node.expression is StringLiteral) {
      target.collect(node.expression as StringLiteral);
    }
    super.visitNamedExpression(node);
  }

  @override
  void visitMethodInvocation(MethodInvocation node) {
    if (['_Fault', 'FormatException'].contains(node.methodName.name)) {
      for (final argument in node.argumentList.arguments) {
        if (argument is StringLiteral) target.collect(argument);
      }
    }
    super.visitMethodInvocation(node);
  }
}

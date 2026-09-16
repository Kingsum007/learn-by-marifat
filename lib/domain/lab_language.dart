enum LabExecution { python, sql, external }

class LabLanguage {
  const LabLanguage(
    this.id,
    this.label,
    this.file,
    this.courseId,
    this.starter, {
    this.execution = LabExecution.external,
  });
  final String id, label, file, courseId, starter;
  final LabExecution execution;
  String get draftId => id == 'python' ? 'playground' : 'lab-$id';
}

const labLanguages = [
  LabLanguage(
    'python',
    'Python',
    'main.py',
    'python',
    'name = "Afghanistan"\nprint("Hello, " + name)\n\nfor n in range(1, 4):\n    print(n)',
    execution: LabExecution.python,
  ),
  LabLanguage(
    'html',
    'HTML',
    'index.html',
    'web-design',
    '<!doctype html>\n<html lang="en">\n<head><meta charset="utf-8"><title>My first page</title></head>\n<body><h1>Salam</h1><p>I am learning.</p></body>\n</html>',
  ),
  LabLanguage(
    'css',
    'CSS',
    'style.css',
    'web-design',
    'body { font-family: sans-serif; margin: 2rem; }\nh1 { color: #102f61; }',
  ),
  LabLanguage(
    'javascript',
    'JavaScript',
    'main.js',
    'javascript',
    'const prices = [10, 20, 30];\nconsole.log(prices.reduce((sum, price) => sum + price, 0));',
  ),
  LabLanguage(
    'java',
    'Java',
    'Main.java',
    'java',
    'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Salam");\n    }\n}',
  ),
  LabLanguage(
    'kotlin',
    'Kotlin',
    'Main.kt',
    'kotlin',
    'fun main() {\n    println("Salam")\n}',
  ),
  LabLanguage(
    'swift',
    'Swift',
    'main.swift',
    'swift',
    'let name = "Afghanistan"\nprint("Salam, \\(name)")',
  ),
  LabLanguage(
    'cpp',
    'C++',
    'main.cpp',
    'cpp',
    '#include <iostream>\nint main() {\n    std::cout << "Salam\\n";\n    return 0;\n}',
  ),
  LabLanguage(
    'dart',
    'Dart',
    'main.dart',
    'flutter-dart',
    'void main() {\n  print("Salam");\n}',
  ),
  LabLanguage(
    'sql',
    'SQL (SQLite)',
    'query.sql',
    'sql',
    'SELECT title, price FROM books ORDER BY id;',
    execution: LabExecution.sql,
  ),
  LabLanguage(
    'postgresql',
    'PostgreSQL',
    'query.sql',
    'postgresql',
    'SELECT current_database(), current_user;',
  ),
  LabLanguage(
    'mongodb',
    'MongoDB',
    'query.js',
    'mongodb',
    'db.books.find({}, {title: 1, _id: 0});',
  ),
  LabLanguage(
    'reactjs',
    'React (JSX)',
    'Greeting.jsx',
    'reactjs',
    'export default function Greeting() {\n  return <h1>Salam</h1>;\n}',
  ),
  LabLanguage(
    'reactnative',
    'React Native',
    'Greeting.jsx',
    'reactnative',
    'import {View, Text} from "react-native";\nexport default function Greeting() {\n  return <View><Text>Salam</Text></View>;\n}',
  ),
  LabLanguage(
    'nodejs',
    'Node.js',
    'main.mjs',
    'nodejs',
    'import {parseArgs} from "node:util";\nconsole.log(parseArgs({allowPositionals: true}).positionals);',
  ),
  LabLanguage(
    'expressjs',
    'Express.js',
    'server.mjs',
    'expressjs',
    'import express from "express";\nconst app = express();\napp.get("/health", (req, res) => res.json({status: "ok"}));\napp.listen(3000, "127.0.0.1");',
  ),
  LabLanguage(
    'android',
    'Android (Kotlin)',
    'Greeting.kt',
    'android',
    'import androidx.compose.runtime.Composable\nimport androidx.compose.material3.Text\n\n@Composable\nfun Greeting() { Text("Salam") }',
  ),
  LabLanguage(
    'ios',
    'iOS (SwiftUI)',
    'Greeting.swift',
    'ios',
    'import SwiftUI\nstruct Greeting: View {\n    var body: some View { Text("Salam") }\n}',
  ),
  LabLanguage(
    'flutter',
    'Flutter',
    'main.dart',
    'flutter-dart',
    'import "package:flutter/material.dart";\nvoid main() => runApp(const MaterialApp(\n  home: Scaffold(body: Center(child: Text("Salam"))),\n));',
  ),
];

Set<String> get labDraftIds => labLanguages.map((l) => l.draftId).toSet();

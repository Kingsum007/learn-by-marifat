import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:learn_by_marifat_team/main.dart' as app;
import 'package:learn_by_marifat_team/presentation/app.dart';
import 'package:learn_by_marifat_team/domain/lab_language.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();
  testWidgets('native startup opens local storage and shows bundled course', (
    tester,
  ) async {
    app.main();
    for (var i = 0; i < 60; i++) {
      await tester.pump(const Duration(milliseconds: 200));
      if (find.byType(HomeShell).evaluate().isNotEmpty) {
        break;
      }
    }
    expect(find.byType(HomeShell), findsOneWidget);
    expect(find.text('Your first step starts here.'), findsOneWidget);
    expect(find.text('100% offline'), findsWidgets);
    await tester.tap(find.text('Courses'));
    await tester.pumpAndSettle();
    expect(find.text('Learn programming step by step'), findsOneWidget);
    await tester.enterText(find.byType(TextField), 'Swift');
    await tester.pumpAndSettle();
    final swiftCourse = find.widgetWithText(ListTile, 'Swift');
    expect(swiftCourse, findsOneWidget);
    await tester.ensureVisible(swiftCourse);
    await tester.tap(swiftCourse);
    await tester.pumpAndSettle();
    expect(find.text('Your mission map'), findsOneWidget);
    await tester.pageBack();
    await tester.pumpAndSettle();
    await tester.tap(find.text('Practice'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Code lab'));
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('code-editor')), findsOneWidget);
    final selector = find.byKey(const Key('lab-language'));
    expect(
      tester.widget<DropdownButton<LabLanguage>>(selector).items!.length,
      19,
    );
    tester.widget<DropdownButton<LabLanguage>>(selector).onChanged!(
      labLanguages.firstWhere((l) => l.id == 'java'),
    );
    await tester.pumpAndSettle();
    expect(find.text('Main.java'), findsOneWidget);
    expect(find.byKey(const Key('run-code')), findsNothing);
    tester.widget<DropdownButton<LabLanguage>>(selector).onChanged!(
      labLanguages.first,
    );
    await tester.pumpAndSettle();
    await tester.ensureVisible(find.byKey(const Key('run-code')));
    await tester.tap(find.byKey(const Key('run-code')));
    await tester.pumpAndSettle();
    expect(find.text('Hello, Afghanistan\n1\n2\n3'), findsOneWidget);
    await tester.pageBack();
    await tester.pumpAndSettle();
    await tester.ensureVisible(find.text('Offline SQL practice'));
    await tester.tap(find.text('Offline SQL practice'));
    await tester.pumpAndSettle();
    await tester.ensureVisible(find.text('Run query'));
    await tester.tap(find.text('Run query'));
    await tester.pumpAndSettle();
    expect(find.byType(DataTable), findsOneWidget);
    expect(find.text('150'), findsOneWidget);
  });
}

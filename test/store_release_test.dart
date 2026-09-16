import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/presentation/about_support_screen.dart';

void main() {
  testWidgets(
    'store build excludes direct financial support and includes privacy text',
    (tester) async {
      await tester.pumpWidget(const MaterialApp(home: AboutSupportScreen()));
      expect(find.text('Support the project'), findsNothing);
      await tester.ensureVisible(find.text('Privacy and learner data'));
      await tester.pumpAndSettle();
      expect(find.text('Privacy and learner data'), findsOneWidget);
      expect(tester.takeException(), isNull);
    },
    skip: !storeBuild,
  );
}

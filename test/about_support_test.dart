import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/presentation/about_support_screen.dart';

void main() {
  testWidgets('support details remain readable with large text', (
    tester,
  ) async {
    tester.view.physicalSize = const Size(360, 800);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(
      MaterialApp(
        builder: (context, child) => MediaQuery(
          data: MediaQuery.of(context)
              .copyWith(textScaler: const TextScaler.linear(1.5)),
          child: child!,
        ),
        home: const AboutSupportScreen(),
      ),
    );
    expect(find.text(hesabPayNumber), findsWidgets);
    expect(find.text('Support the project'), findsOneWidget);
    await tester.ensureVisible(find.text('Safi Ullah Mirzai'));
    await tester.pumpAndSettle();
    expect(find.text('Safi Ullah Mirzai'), findsOneWidget);
    await tester.ensureVisible(find.text(founderEmail));
    await tester.pumpAndSettle();
    expect(find.text(founderEmail), findsOneWidget);
    expect(find.text(founderWebsite), findsOneWidget);
    await tester.ensureVisible(find.text('Code With Safi'));
    await tester.pumpAndSettle();
    expect(find.text(youtubeChannelUrl), findsOneWidget);
    expect(find.text('Open YouTube channel'), findsOneWidget);
    expect(find.text('About Marifat Team'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
}

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
import 'package:learn_by_marifat_team/data/translations.dart';
import 'package:learn_by_marifat_team/presentation/app.dart';

import 'support.dart';

void main() {
  setUpAll(() async {
    await (FontLoader('LearnSans')
          ..addFont(rootBundle.load('assets/fonts/roboto-regular.ttf'))
          ..addFont(rootBundle.load('assets/fonts/roboto-bold.ttf'))
          ..addFont(rootBundle.load('assets/fonts/roboto-black.ttf')))
        .load();
    await (FontLoader(
      'LearnArabic',
    )..addFont(rootBundle.load('assets/fonts/noto-naskh-arabic.ttf'))).load();
    await (FontLoader(
      'MaterialIcons',
    )..addFont(rootBundle.load('fonts/MaterialIcons-Regular.otf'))).load();
  });

  for (final language in ['en', 'fa', 'ps']) {
    testWidgets('$language Microsoft Store desktop screenshots', (
      tester,
    ) async {
      tester.view.physicalSize = const Size(1440, 900);
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);
      final controller = LearningController(
        courses: BundledCourse(),
        curriculum: const BundledCurriculum(),
        progress: MemoryProgress(),
        runner: TestRunner(),
      );
      addTearDown(controller.dispose);
      await controller.preferences(language: language);
      await tester.pumpWidget(
        RepaintBoundary(
          key: const Key('microsoft-store-capture'),
          child: LearnApp(controller: controller),
        ),
      );
      await tester.pumpAndSettle();
      await tester.runAsync(
        () => precacheImage(
          const AssetImage('assets/brand/marifat.png'),
          tester.element(find.byType(MaterialApp).first),
        ),
      );
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);
      await expectLater(
        find.byKey(const Key('microsoft-store-capture')),
        matchesGoldenFile(
          '../distribution/microsoft-store/assets/screenshots/home-$language.png',
        ),
      );

      await tester.tap(find.text(translate('Courses', language)));
      await tester.pumpAndSettle();
      expect(tester.takeException(), isNull);
      await expectLater(
        find.byKey(const Key('microsoft-store-capture')),
        matchesGoldenFile(
          '../distribution/microsoft-store/assets/screenshots/courses-$language.png',
        ),
      );
    });
  }
}

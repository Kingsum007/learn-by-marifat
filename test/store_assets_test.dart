import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:learn_by_marifat_team/application/learning_controller.dart';
import 'package:learn_by_marifat_team/data/bundled_course.dart';
import 'package:learn_by_marifat_team/data/bundled_curriculum.dart';
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

  LearningController model() => LearningController(
    courses: BundledCourse(),
    curriculum: const BundledCurriculum(),
    progress: MemoryProgress(),
    runner: TestRunner(),
  );

  testWidgets('English phone store screenshots', (tester) async {
    tester.view.physicalSize = const Size(450, 900);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    final controller = model();
    addTearDown(controller.dispose);

    await tester.pumpWidget(
      RepaintBoundary(
        key: const Key('store-capture'),
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
      find.byKey(const Key('store-capture')),
      matchesGoldenFile('../distribution/google-play/assets/phone-home-en.png'),
    );

    await tester.tap(find.text('Courses'));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
    await expectLater(
      find.byKey(const Key('store-capture')),
      matchesGoldenFile(
        '../distribution/google-play/assets/phone-courses-en.png',
      ),
    );
  });
}

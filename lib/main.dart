import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

import 'presentation/learning_localizations.dart';

import 'package:path/path.dart' as path;
import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqflite.dart' show databaseFactorySqflitePlugin;
import 'package:sqflite_common_ffi/sqflite_ffi.dart';

import 'application/learning_controller.dart';
import 'data/bundled_course.dart';
import 'data/bundled_curriculum.dart';
import 'data/sqlite_progress_repository.dart';
import 'presentation/app.dart';
import 'presentation/theme.dart';
import 'presentation/localized_text.dart';
import 'runtime/code_runner.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  LicenseRegistry.addLicense(() async* {
    yield LicenseEntryWithLineBreaks([
      'Roboto fonts',
    ], await rootBundle.loadString('assets/fonts/LICENSE.txt'));
    yield LicenseEntryWithLineBreaks([
      'Noto Naskh Arabic',
    ], await rootBundle.loadString('assets/fonts/OFL-NotoNaskhArabic.txt'));
  });
  runApp(const Bootstrap());
}

class Bootstrap extends StatefulWidget {
  const Bootstrap({super.key});
  @override
  State<Bootstrap> createState() => _BootstrapState();
}

class _BootstrapState extends State<Bootstrap> {
  LearningController? controller;
  bool failed = false;
  @override
  void initState() {
    super.initState();
    initialize();
  }

  Future<void> initialize() async {
    setState(() => failed = false);
    SqliteProgressRepository? repository;
    try {
      final courses = BundledCourse();
      const curriculum = BundledCurriculum();
      final DatabaseFactory factory;
      if (Platform.isWindows || Platform.isLinux) {
        sqfliteFfiInit();
        factory = databaseFactoryFfi;
      } else {
        factory = databaseFactorySqflitePlugin;
      }
      final applicationDirectory = await getApplicationSupportDirectory();
      // Keep the established Windows storage location across the display rename.
      final directory = Platform.isWindows
          ? Directory(
              path.join(path.dirname(applicationDirectory.path), 'kohi'),
            )
          : applicationDirectory;
      await directory.create(recursive: true);
      repository = await SqliteProgressRepository.open(
        factory,
        path.join(directory.path, 'kohi.db'),
        courses,
        curriculum: curriculum,
      );
      final model = LearningController(
        courses: courses,
        curriculum: curriculum,
        progress: repository,
        runner: IsolateCodeRunner(),
      );
      await model.initialize();
      if (mounted) {
        setState(() => controller = model);
      } else {
        model.dispose();
        await repository.close();
      }
    } catch (error, stack) {
      if (kDebugMode) {
        debugPrint('Learn By Marifat Team startup failed: $error\n$stack');
      }
      await repository?.close();
      if (mounted) {
        setState(() => failed = true);
      }
    }
  }

  @override
  Widget build(BuildContext context) => controller != null
      ? LearnApp(controller: controller!)
      : MaterialApp(
          supportedLocales: const [Locale('en'), Locale('fa'), Locale('ps')],
          localizationsDelegates: learningLocalizations,
          debugShowCheckedModeBanner: false,
          theme: learnTheme(false),
          home: Scaffold(
            body: Center(
              child: Padding(
                padding: const EdgeInsets.all(32),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Brand(),
                    const SizedBox(height: 24),
                    if (!failed)
                      const CircularProgressIndicator()
                    else ...[
                      const LText(
                        'Your saved data could not be opened. No data has been erased. Check available storage and try again.',
                        textAlign: TextAlign.center,
                      ),
                      const SizedBox(height: 16),
                      FilledButton(
                        onPressed: initialize,
                        child: const LText('Try again'),
                      ),
                    ],
                  ],
                ),
              ),
            ),
          ),
        );
}

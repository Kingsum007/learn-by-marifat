import 'package:flutter/material.dart';

import '../application/learning_controller.dart';
import 'localized_text.dart';

class TopicGate extends StatelessWidget {
  const TopicGate({
    super.key,
    required this.controller,
    required this.allowed,
    required this.child,
  });
  final LearningController controller;
  final bool Function() allowed;
  final Widget child;
  @override
  Widget build(BuildContext context) => ListenableBuilder(
    listenable: controller,
    builder: (context, _) => allowed()
        ? child
        : Scaffold(
            appBar: AppBar(title: const LText('Topic locked')),
            body: const Center(
              child: Padding(
                padding: EdgeInsets.all(24),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.lock_outline, size: 48),
                    SizedBox(height: 20),
                    LText(
                      'Finish the required earlier course or topic first. For Python foundations, solve every challenge. For workshops, save evidence and confirm completion in both practice activities. Projects unlock after the workshops.',
                      textAlign: TextAlign.center,
                    ),
                  ],
                ),
              ),
            ),
          ),
  );
}

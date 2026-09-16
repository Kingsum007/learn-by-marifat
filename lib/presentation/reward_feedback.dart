import 'package:flutter/material.dart';

import 'localized_text.dart';

class RewardFeedback extends StatelessWidget {
  const RewardFeedback({super.key, required this.points});
  final int points;
  @override
  Widget build(BuildContext context) => TweenAnimationBuilder<double>(
    tween: Tween(begin: .85, end: 1),
    duration: const Duration(milliseconds: 450),
    builder: (_, value, child) => Transform.scale(scale: value, child: child),
    child: Container(
      margin: const EdgeInsets.symmetric(vertical: 16),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.primaryContainer,
        borderRadius: BorderRadius.circular(24),
      ),
      child: Row(
        children: [
          const Icon(
            Icons.emoji_events_rounded,
            color: Color(0xFFCC8500),
            size: 48,
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                LText(
                  '+$points XP earned',
                  style: const TextStyle(
                    fontSize: 23,
                    fontWeight: FontWeight.w900,
                  ),
                ),
                const LText('Challenge completed. Keep your adventure going!'),
              ],
            ),
          ),
        ],
      ),
    ),
  );
}

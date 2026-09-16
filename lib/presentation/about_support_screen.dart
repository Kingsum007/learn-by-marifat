import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:url_launcher/url_launcher.dart';

import 'localized_text.dart';
import 'theme.dart';

const hesabPayNumber = '+93788070101';
const founderEmail = 'sumirzai@gmail.com';
const founderWebsite = 'safimirzai.dev';
const founderLinkedIn = 'linkedin.com/in/kingsum007';
const founderGitHub = 'github.com/Kingsum007';
const youtubeChannelUrl = 'https://www.youtube.com/@codewithsafi-sum';
const storeBuild = bool.fromEnvironment('STORE_BUILD');

class AboutSupportScreen extends StatelessWidget {
  const AboutSupportScreen({super.key});

  Future<void> copy(BuildContext context, String value, String message) async {
    await Clipboard.setData(ClipboardData(text: value));
    if (context.mounted) {
      ScaffoldMessenger.of(context)
          .showSnackBar(SnackBar(content: LText(message)));
    }
  }

  Future<void> openYouTube(BuildContext context) async {
    final opened = await launchUrl(
      Uri.parse(youtubeChannelUrl),
      mode: LaunchMode.externalApplication,
    );
    if (!opened && context.mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: LText('Could not open the YouTube channel')),
      );
    }
  }

  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const LText('About and support')),
    body: _SupportPageBody(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const PageHeading(
            'Marifat Software Team',
            'Learn, build, and help others learn.',
            'Learn By Marifat Team is designed for Afghan students who need clear programming education that remains available without internet.',
          ),
          if (!storeBuild) ...[
            Card(
              color: Theme.of(context).colorScheme.primaryContainer,
              child: Padding(
                padding: const EdgeInsets.all(24),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Icon(Icons.volunteer_activism_outlined, size: 38),
                    const SizedBox(height: 14),
                    const LText(
                      'Support the project',
                      style: TextStyle(
                        fontSize: 22,
                        fontWeight: FontWeight.w900,
                      ),
                    ),
                    const SizedBox(height: 10),
                    const LText(
                      'Your voluntary contribution helps Marifat Team improve offline lessons, translations, testing, and learning resources. Learning content remains available without a donation.',
                      style: TextStyle(height: 1.7),
                    ),
                    const SizedBox(height: 18),
                    const LText(
                      'HesabPay',
                      style: TextStyle(fontWeight: FontWeight.w800),
                    ),
                    const SizedBox(height: 6),
                    const Directionality(
                      textDirection: TextDirection.ltr,
                      child: SelectableText(
                        hesabPayNumber,
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                    ),
                    const SizedBox(height: 14),
                    FilledButton.icon(
                      onPressed: () => copy(
                        context,
                        hesabPayNumber,
                        'HesabPay number copied',
                      ),
                      icon: const Icon(Icons.copy_outlined),
                      label: const LText('Copy HesabPay number'),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),
          ],
          const _AboutCard(
            icon: Icons.groups_2_outlined,
            title: 'About Marifat Team',
            body: 'Marifat Software Team builds practical software and educational tools. This project focuses on understandable, project-based programming education for Afghanistan, with English, Dari, and Pashto content stored on the learner’s device.',
          ),
          const SizedBox(height: 16),
          const _AboutCard(
            icon: Icons.person_outline,
            title: 'Safi Ullah Mirzai',
            body: 'Founder of Marifat Software Team, senior full-stack developer, and computer science lecturer in Kabul. He teaches databases, programming, mobile application development, software engineering, computer architecture, and software assurance. He holds a bachelor’s degree in Computer Science (Software Engineering) and is pursuing a master’s degree in Information Systems at Kabul University. His work includes educational tools, management information systems, web applications, mobile development, and database systems.',
          ),
          const SizedBox(height: 16),
          _ContactCard(
            onCopy: (value) => copy(context, value, 'Contact copied'),
          ),
          const SizedBox(height: 16),
          _YouTubeCard(
            onOpen: () => openYouTube(context),
            onCopy: () =>
                copy(context, youtubeChannelUrl, 'YouTube link copied'),
          ),
          const SizedBox(height: 16),
          const _AboutCard(
            icon: Icons.privacy_tip_outlined,
            title: 'Privacy and learner data',
            body: 'The app has no account, advertising, analytics, or remote server. Lessons, progress, answers, drafts, and portfolio notes stay on this device. The app does not transmit learner data. You choose when and where to export a local backup. Opening the YouTube channel leaves the app and follows the privacy terms of the external service.',
          ),
        ],
      ),
    ),
  );
}

class _YouTubeCard extends StatelessWidget {
  const _YouTubeCard({required this.onOpen, required this.onCopy});

  final VoidCallback onOpen, onCopy;

  @override
  Widget build(BuildContext context) => Card(
    child: Padding(
      padding: const EdgeInsets.all(22),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              Icon(
                Icons.ondemand_video_outlined,
                color: Theme.of(context).colorScheme.primary,
                size: 30,
              ),
              const SizedBox(width: 16),
              const Expanded(
                child: LText(
                  'Code With Safi',
                  style: TextStyle(fontSize: 19, fontWeight: FontWeight.w900),
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          const LText(
            'Watch programming lessons and practical tutorials on the official YouTube channel. Opening YouTube requires internet; the courses in this app remain offline.',
            style: TextStyle(height: 1.7),
          ),
          const SizedBox(height: 10),
          const Directionality(
            textDirection: TextDirection.ltr,
            child: SelectableText(youtubeChannelUrl),
          ),
          const SizedBox(height: 14),
          Wrap(
            spacing: 10,
            runSpacing: 10,
            children: [
              FilledButton.icon(
                onPressed: onOpen,
                icon: const Icon(Icons.open_in_new),
                label: const LText('Open YouTube channel'),
              ),
              OutlinedButton.icon(
                onPressed: onCopy,
                icon: const Icon(Icons.copy_outlined),
                label: const LText('Copy channel link'),
              ),
            ],
          ),
        ],
      ),
    ),
  );
}

class _ContactCard extends StatelessWidget {
  const _ContactCard({required this.onCopy});

  final ValueChanged<String> onCopy;

  @override
  Widget build(BuildContext context) => Card(
    child: Padding(
      padding: const EdgeInsets.all(22),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              Icon(
                Icons.contact_mail_outlined,
                color: Theme.of(context).colorScheme.primary,
                size: 30,
              ),
              const SizedBox(width: 16),
              const Expanded(
                child: LText(
                  'Contact Marifat Team',
                  style: TextStyle(fontSize: 19, fontWeight: FontWeight.w900),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          const LText(
            'Use the copy button to save a contact address. Opening websites and social pages requires internet access.',
            style: TextStyle(height: 1.6),
          ),
          const SizedBox(height: 12),
          for (final entry in const [
            ('Email', founderEmail, Icons.email_outlined),
            ('Website', founderWebsite, Icons.language_outlined),
            ('LinkedIn', founderLinkedIn, Icons.badge_outlined),
            ('GitHub', founderGitHub, Icons.code_outlined),
            ('Phone and WhatsApp', hesabPayNumber, Icons.chat_outlined),
          ])
            _ContactRow(
              label: entry.$1,
              value: entry.$2,
              icon: entry.$3,
              onCopy: onCopy,
            ),
        ],
      ),
    ),
  );
}

class _ContactRow extends StatelessWidget {
  const _ContactRow({
    required this.label,
    required this.value,
    required this.icon,
    required this.onCopy,
  });

  final String label, value;
  final IconData icon;
  final ValueChanged<String> onCopy;

  @override
  Widget build(BuildContext context) => Padding(
    padding: const EdgeInsets.symmetric(vertical: 5),
    child: DecoratedBox(
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.surfaceContainerHighest,
        borderRadius: BorderRadius.circular(16),
      ),
      child: Padding(
        padding: const EdgeInsetsDirectional.fromSTEB(14, 8, 8, 8),
        child: Row(
          children: [
            Icon(icon, size: 21),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  LText(
                    label,
                    style: const TextStyle(fontWeight: FontWeight.w800),
                  ),
                  const SizedBox(height: 2),
                  Directionality(
                    textDirection: TextDirection.ltr,
                    child: SelectableText(value),
                  ),
                ],
              ),
            ),
            IconButton(
              tooltip: 'Copy contact',
              onPressed: () => onCopy(value),
              icon: const Icon(Icons.copy_outlined),
            ),
          ],
        ),
      ),
    ),
  );
}

class _SupportPageBody extends StatelessWidget {
  const _SupportPageBody({required this.child});

  final Widget child;

  @override
  Widget build(BuildContext context) => SingleChildScrollView(
    child: Center(
      child: Container(
        constraints: const BoxConstraints(maxWidth: 920),
        padding: EdgeInsets.all(
          MediaQuery.sizeOf(context).width < 600 ? 20 : 40,
        ),
        child: child,
      ),
    ),
  );
}

class _AboutCard extends StatelessWidget {
  const _AboutCard({
    required this.icon,
    required this.title,
    required this.body,
  });
  final IconData icon;
  final String title, body;
  @override
  Widget build(BuildContext context) => Card(
    child: Padding(
      padding: const EdgeInsets.all(22),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(icon, color: Theme.of(context).colorScheme.primary, size: 30),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                LText(
                  title,
                  style: const TextStyle(
                    fontSize: 19,
                    fontWeight: FontWeight.w900,
                  ),
                ),
                const SizedBox(height: 8),
                LText(body, style: const TextStyle(height: 1.7)),
              ],
            ),
          ),
        ],
      ),
    ),
  );
}

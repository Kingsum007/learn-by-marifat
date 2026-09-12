/// A guided teaching-core exercise plus a separate full-toolchain reference.
class ProjectGuide {
  ProjectGuide(Map<String, dynamic> data)
    : steps = List<String>.unmodifiable(data['steps'] as List),
      starter = data['starter'] as String,
      solution = data['solution'] as String,
      expected = data['expected'] as String,
      file = data['file'] as String,
      commands = data['commands'] as String,
      reference = data['reference'] as String;
  final List<String> steps;
  final String starter, solution, expected, file, commands, reference;
}

/// Read-only curriculum port. Content is bundled; no connectivity is required.
abstract interface class CurriculumRepository {
  List<StudyCourse> get catalog;
}

enum BloomLevel { remember, understand, apply, analyze, evaluate, create }

class StudyCourse {
  StudyCourse(Map<String, dynamic> json)
    : id = json['id'] as String,
      title = json['title'] as String,
      tools = json['tools'] as String,
      beginner = BeginnerLesson(json['beginner'] as Map<String, dynamic>),
      prerequisites = List<String>.unmodifiable(json['prerequisites'] as List),
      modules = List.unmodifiable(
        (json['modules'] as List).map(
          (e) => StudyModule(e as Map<String, dynamic>),
        ),
      ),
      projects = List.unmodifiable(
        (json['projects'] as List).map(
          (e) => StudyProject(e as Map<String, dynamic>),
        ),
      );
  final String id, title, tools;
  final BeginnerLesson beginner;
  final List<String> prerequisites;
  final List<StudyModule> modules;
  final List<StudyProject> projects;
}

class BeginnerLesson {
  BeginnerLesson(Map<String, dynamic> data)
    : terms = List<String>.unmodifiable(data['terms'] as List),
      before = data['before'] as String,
      code = data['code'] as String,
      trace = List<String>.unmodifiable(data['trace'] as List),
      question = data['question'] as String,
      options = List<String>.unmodifiable(data['options'] as List),
      answer = data['answer'] as int,
      task = data['task'] as String,
      hint = data['hint'] as String,
      solution = data['solution'] as String,
      result = data['result'] as String;
  final List<String> terms, trace, options;
  final String before, code, question, task, hint, solution, result;
  final int answer;
}

class StudyModule {
  StudyModule(Map<String, dynamic> json)
    : title = json['title'] as String,
      explanation = json['explanation'] as String,
      practice = json['practice'] as String,
      example = json['example'] as String,
      plans = List.unmodifiable(
        (json['plans'] as List).map(
          (e) => LessonPlan(e as Map<String, dynamic>),
        ),
      );
  final String title, explanation, example, practice;
  final List<LessonPlan> plans;
}

class LessonPlan {
  LessonPlan(Map<String, dynamic> json)
    : id = json['id'] as String,
      title = json['title'] as String,
      objective = json['objective'] as String,
      activity = json['activity'] as String,
      evidence = json['evidence'] as String,
      level = BloomLevel.values.byName(json['level'] as String),
      minutes = json['minutes'] as int;
  final String id, title, objective, activity, evidence;
  final BloomLevel level;
  final int minutes;
}

class StudyProject {
  StudyProject(Map<String, dynamic> json)
    : id = json['id'] as String,
      title = json['title'] as String,
      brief = json['brief'] as String,
      hours = json['hours'] as int,
      requirements = List<String>.unmodifiable(json['requirements'] as List),
      milestones = List<String>.unmodifiable(json['milestones'] as List);
  final String id, title, brief;
  final int hours;
  final List<String> requirements, milestones;
}

Set<String> portfolioIds(CurriculumRepository repository) => {
  for (final course in repository.catalog) ...[
    for (final module in course.modules)
      for (final plan in module.plans) plan.id,
    for (final project in course.projects) project.id,
  ],
};

import 'package:flutter/cupertino.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

const learningLocalizations = <LocalizationsDelegate<dynamic>>[
  PashtoCupertinoDelegate(),
  ...GlobalMaterialLocalizations.delegates,
];

/// Flutter supplies Pashto Material strings but no Pashto Cupertino delegate.
class PashtoCupertinoDelegate
    extends LocalizationsDelegate<CupertinoLocalizations> {
  const PashtoCupertinoDelegate();
  @override
  bool isSupported(Locale locale) => locale.languageCode == 'ps';
  @override
  Future<CupertinoLocalizations> load(Locale locale) =>
      SynchronousFuture(const PashtoCupertinoLocalizations());
  @override
  bool shouldReload(PashtoCupertinoDelegate old) => false;
}

class PashtoCupertinoLocalizations extends DefaultCupertinoLocalizations {
  const PashtoCupertinoLocalizations();
  static const months = [
    'جنوري',
    'فبروري',
    'مارچ',
    'اپرېل',
    'مې',
    'جون',
    'جولای',
    'اګست',
    'سپتمبر',
    'اکتوبر',
    'نومبر',
    'دسمبر',
  ];
  static const days = [
    'دوشنبه',
    'سه‌شنبه',
    'چهارشنبه',
    'پنجشنبه',
    'جمعه',
    'شنبه',
    'یکشنبه',
  ];
  @override
  String datePickerMonth(int monthIndex) => months[monthIndex - 1];
  @override
  String datePickerStandaloneMonth(int monthIndex) =>
      datePickerMonth(monthIndex);
  @override
  String datePickerDayOfMonth(int dayIndex, [int? weekDay]) =>
      weekDay == null ? '$dayIndex' : '${days[weekDay - 1]} $dayIndex';
  @override
  String datePickerHourSemanticsLabel(int hour) => '$hour بجې';
  @override
  String datePickerMinuteSemanticsLabel(int minute) => '$minute دقیقې';
  @override
  String datePickerMediumDate(DateTime date) =>
      '${days[date.weekday - 1]}، ${date.day} ${months[date.month - 1]}';
  @override
  String get anteMeridiemAbbreviation => 'له غرمې مخکې';
  @override
  String get postMeridiemAbbreviation => 'له غرمې وروسته';
  @override
  String get todayLabel => 'نن';
  @override
  String get alertDialogLabel => 'خبرتیا';
  @override
  String tabSemanticsLabel({required int tabIndex, required int tabCount}) =>
      'له $tabCount څخه $tabIndex ټب';
  @override
  String timerPickerHourLabel(int hour) => 'ساعت';
  @override
  String timerPickerMinuteLabel(int minute) => 'دقیقې';
  @override
  String timerPickerSecondLabel(int second) => 'ثانیې';
  @override
  String get cutButtonLabel => 'پرې کول';
  @override
  String get copyButtonLabel => 'کاپي';
  @override
  String get pasteButtonLabel => 'نښلول';
  @override
  String get clearButtonLabel => 'پاکول';
  @override
  String get noSpellCheckReplacementsLabel => 'بدیل ونه موندل شو';
  @override
  String get selectAllButtonLabel => 'ټول ټاکل';
  @override
  String get lookUpButtonLabel => 'پلټل';
  @override
  String get searchWebButtonLabel => 'وېب لټول';
  @override
  String get shareButtonLabel => 'شریکول';
  @override
  String get searchTextFieldPlaceholderLabel => 'لټون';
  @override
  String get modalBarrierDismissLabel => 'بندول';
  @override
  String get menuDismissLabel => 'مېنو بندول';
  @override
  String get cancelButtonLabel => 'لغوه';
  @override
  String get backButtonLabel => 'شاته';
  @override
  String get expansionTileExpandedHint => 'د تړلو لپاره دوه ځله کېکاږئ';
  @override
  String get expansionTileCollapsedHint => 'د پرانیستلو لپاره دوه ځله کېکاږئ';
  @override
  String get expansionTileExpandedTapHint => 'تړل';
  @override
  String get expansionTileCollapsedTapHint => 'د نورو معلوماتو لپاره پرانیستل';
  @override
  String get expandedHint => 'تړل شوی';
  @override
  String get collapsedHint => 'پرانیستی';
}

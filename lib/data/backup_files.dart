import 'dart:convert';
import 'dart:typed_data';

import 'package:file_picker/file_picker.dart';

class BackupFiles {
  Future<bool> export(
    String source, {
    String title = 'Save Learn By Marifat Team backup',
  }) async {
    final uri = await FilePicker.saveFile(
      dialogTitle: title,
      fileName: 'learn-by-marifat-team-backup.json',
      mimeType: 'application/json',
      bytes: Uint8List.fromList(utf8.encode(source)),
    );
    return uri != null;
  }

  Future<String?> import({
    String title = 'Open Learn By Marifat Team backup',
  }) async {
    final selected = await FilePicker.pickFile(
      dialogTitle: title,
      type: FileType.custom,
      allowedExtensions: ['json'],
    );
    if (selected == null) {
      return null;
    }
    if ((selected.lengthSync() ?? 0) > 16000000) {
      throw const FormatException('Backup exceeds 16 MB.');
    }
    final buffer = BytesBuilder(copy: false);
    await for (final chunk in selected.readAsByteStream()) {
      if (buffer.length + chunk.length > 16000000) {
        throw const FormatException('Backup exceeds 16 MB.');
      }
      buffer.add(chunk);
    }
    try {
      return utf8.decode(buffer.takeBytes());
    } on FormatException {
      throw const FormatException('Backup is not valid UTF-8.');
    }
  }
}

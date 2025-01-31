import os
import shutil
import datetime

def backupComposeFiles(source, destination, keep):
    """Backup für docker-compose.yml Dateien."""
    backupYamlFiles(source, destination, keep, only_compose=True)

def backupYamlFiles(source, destination, keep, only_compose=False):
    """Backup für alle .yaml und .yml Dateien (außer docker-compose.yml falls only_compose=False)."""
    
    # Zeitstempel für den Backup-Ordner erstellen
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    backup_folder = os.path.join(destination, timestamp)
    os.makedirs(backup_folder, exist_ok=True)

    # Backup durchführen
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                if only_compose and file != "docker-compose.yml":
                    continue  # Überspringe alle außer docker-compose.yml
                if not only_compose and file == "docker-compose.yml":
                    continue  # Überspringe nur docker-compose.yml

                source_file_path = os.path.join(root, file)

                # Zielverzeichnis mit Ordnerstruktur
                relative_path = os.path.relpath(root, source)
                target_directory = os.path.join(backup_folder, relative_path)
                os.makedirs(target_directory, exist_ok=True)

                # Datei kopieren
                target_file_path = os.path.join(target_directory, file)
                shutil.copy2(source_file_path, target_file_path)
                print(f"copying: {source_file_path} -> {target_file_path}")

    # Älteste Backups löschen, falls mehr als 'keep' existieren
    existing_backups = sorted(
        [d for d in os.listdir(destination) if os.path.isdir(os.path.join(destination, d))],
        key=lambda d: os.path.getctime(os.path.join(destination, d))
    )

    while len(existing_backups) > keep:
        oldest_backup = existing_backups.pop(0)
        oldest_backup_path = os.path.join(destination, oldest_backup)
        shutil.rmtree(oldest_backup_path)
        print(f"Deleted old backup: {oldest_backup_path}")

# Beispielaufruf:
# backupComposeFiles("/pfad/zur/quelle", "/pfad/zum/backup", 5)  # Nur docker-compose.yml sichern
# backupYamlFiles("/pfad/zur/quelle", "/pfad/zum/backup", 5, only_compose=False)  # Alle YAMLs außer docker-compose.yml sichern

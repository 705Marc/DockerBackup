import os
import shutil

# Folder of your docker containers
source_folder = "/docker"

# Zielordner, in den die Dateien kopiert werden sollen
destination_folder = "/path/to/target"  # BackupFolder

# Sicherstellen, dass der Zielordner existiert
os.makedirs(destination_folder, exist_ok=True)

def copy_docker_compose_files(source, destination):
    for root, dirs, files in os.walk(source):
        for file in files:
            if file == "docker-compose.yml":
                source_file_path = os.path.join(root, file)
                
                # target path with folder structure
                relative_path = os.path.relpath(root, source)
                target_directory = os.path.join(destination, relative_path)
                os.makedirs(target_directory, exist_ok=True)

                # copy the files
                target_file_path = os.path.join(target_directory, file)
                shutil.copy2(source_file_path, target_file_path)
                print(f"copying: {source_file_path} -> {target_file_path}")

if __name__ == "__main__":
    copy_docker_compose_files(source_folder, destination_folder)
    print("Backup completed!")

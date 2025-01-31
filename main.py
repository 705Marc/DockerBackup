import backup

import yaml

def load_settings(file_path="settings.yml"):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
    
settings = load_settings()   
    
    



if __name__ == "__main__":
    backup.backupYamlFiles(settings["sourceFolder"], settings["destinationFolder"]+"/"+settings["compose"]["backupFolder"],settings["compose"]["keep"], only_compose=True)
    backup.backupYamlFiles(settings["sourceFolder"], settings["destinationFolder"]+"/"+settings["config"]["backupFolder"],settings["config"]["keep"], only_compose=False)
    print("Backup completed!")
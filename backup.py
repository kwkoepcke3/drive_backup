#!/usr/bin/env python
import os
import subprocess

BACKUPS=os.getenv("DRIVE_BACKUPS_LIST", "backup.cfg")
REMOTE=os.getenv("DRIVE_BACKUPS_REMOTE", "drive_backup")

def main():
    with open(BACKUPS, "r") as f:
        backup_list = f.read().splitlines()
        backup_list = list(map(lambda backup: backup.split(":"), backup_list))
        
    for local_dir, rclone_dir in backup_list:
        print(f"Putting {local_dir} in {REMOTE}:{rclone_dir}...")
        subprocess.run(["rclone", "copy", local_dir, f"{REMOTE}:{rclone_dir}"], capture_output=True, check=True)
        print("Done!")
        

if __name__ == "__main__":
    main()

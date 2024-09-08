#!/bin/bash

# Variables
SOURCE_DIR="/home/aviral/documents"
REMOTE_SERVER="aviral@backupserver.com:/backups/documents/"
LOG_FILE="/home/aviral/backup.log"

# Function to perform backup
backup() {
    rsync -avz --delete $SOURCE_DIR $REMOTE_SERVER

    if [ $? -eq 0 ]; then
        echo "$(date): Backup successful" >> $LOG_FILE
    else
        echo "$(date): Backup failed" >> $LOG_FILE
    fi
}

# Call the backup function
backup

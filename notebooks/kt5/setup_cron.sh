#!/bin/bash

# Путь до ETL скрипта
ETL_SCRIPT="./etl_to_hdfs.py"
LOG_FILE="./etl.log"

# Команда cron
CRON_JOB="*/5 * * * * /usr/bin/python3 $ETL_SCRIPT >> $LOG_FILE 2>&1"

# Проверяем, есть ли уже такая задача
crontab -l 2>/dev/null | grep -F "$ETL_SCRIPT" >/dev/null
if [ $? -eq 0 ]; then
    echo "Cron-задача уже существует."
else
    # Добавляем новую задачу
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "Cron-задача добавлена."
fi

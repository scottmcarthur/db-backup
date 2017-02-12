#Installation

    apt-get install python python-pip
    pip install boto3
    mkdir -p ~/db-backup && cd "$_"
    wget -O backup.py https://raw.githubusercontent.com/scottmcarthur/db-backup/master/backup.py
    chmod +x ./backup.py

##Crontab

    0 */6 * * * /usr/bin/mysqldump -u <username> -p<password> <database> | gzip > /root/db-backup/db.sql.gz; /root/db-backup/backup.py /root/db-backup/db.sql.gz <bucket> <database> <aws-id> <aws-key> >/dev/null 2>&1

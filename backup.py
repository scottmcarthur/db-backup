#!/usr/bin/python
__author__ = 'element220'
import sys
import datetime
import os
import boto3

#Usage ./backup.py <path> <bucket-name> <db-name>

if len(sys.argv) != 6:
  quit()

source_path = str(sys.argv[1])
source_size = os.stat(source_path).st_size
doy = datetime.datetime.now().timetuple().tm_yday
bucket = str(sys.argv[2])
name = str(sys.argv[3])
key = "db/%s/%s.sql.gz" % (name,doy)

print ("File: %s (%s bytes)" % (source_path, source_size))
print ("DOY: %s" % doy)
print ("Bucket: %s" % doy)
print ("Key: %s" % key)

s3_client = boto3.client("s3",aws_access_key_id=str(sys.argv[4]),aws_secret_access_key=str(sys.argv[5]))
s3_client.upload_file(source_path, bucket, key)
print ("Completed")
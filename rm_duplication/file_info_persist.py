import redis
import json


r = redis.StrictRedis(host='localhost', port=6379, db=0)

def store_file_info(src_set, duplicate_hash, json_str):
    file_json = json.loads(json_str)
    file_name = file_json['name']
    print(file_name)
    if r.sismember(src_set, file_name):
        print('find file %s' % (file_name))
        store_dup_files_info(duplicate_hash, file_json)
    else:
        r.sadd(src_set,file_name)


def store_dup_files_info(dup_hash, file_json):
    dup_file_name = file_json['name']
    dup_file_path = file_json['path']
    if r.hset(dup_hash, dup_file_path + '/' + dup_file_name, file_json) == 0 :
        print('File (%s) has been existed in %s' % (dup_file_path + '/' + dup_file_name, dup_hash))


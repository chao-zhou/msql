import fnmatch
import os
import re
import config

num_pattern = "([0-9]+).sql"


def get_max_file_num(pattern):
    update_folder_path = os.path.join(config.BASE_DIR, config.PATH_SCHEMA_UPDATE_FOLDER)
    max_num = -1
    for file in os.listdir(update_folder_path):
        if fnmatch.fnmatch(file, pattern):
            match = re.search(num_pattern, file)
            match_num = int(match.group(1))
            max_num = max(max_num, match_num)

    return max_num


def get_branch_sql_files(pattern):
    update_folder_path = os.path.join(config.BASE_DIR, config.PATH_SCHEMA_UPDATE_FOLDER)
    return [f for f in os.listdir(update_folder_path) if fnmatch.fnmatch(f, pattern)]

import os

import config
from git import git_mv
from msql import sqlfiles
from msql.pattern import *


class RenameBranchSQLFiles:
    def __init__(self, project_file):
        if not project_file.loaded:
            project_file.load()

        self.project_file = project_file

    def rename_branch_sql_files(self):
        print("Rename [Update] SQL Files And Update Project File")
        u_num = self.__rename_sql_files(UPDATE_SQL_FILE_PATTERN)

        print("Rename [Conversion] SQL Files And Update Project File")
        c_num = self.__rename_sql_files(CONVERSION_SQL_FILE_PATTERN)

        print("Rename [Metric SQL] Files And Update Project File")
        m_num = self.__rename_sql_files(METRIC_SQL_FILE_PATTERN)

        print("Update [CurrentVersion.txt] {0}\{1}\{2}".format(u_num, c_num, m_num))
        self.__update_current_version_files(u_num, c_num, m_num)

    def __rename_sql_files(self, file_pattern):
        num = sqlfiles.get_max_file_num(file_pattern.search_pattern)
        for f in sqlfiles.get_branch_sql_files(file_pattern.branch_search_pattern):
            num += 1
            self.__rename_sql_file(f, file_pattern.output_file_format.format(num))
        return num

    def __rename_sql_file(self, src_name, dst_name):
        update_folder_path = os.path.join(config.BASE_DIR, config.PATH_SCHEMA_UPDATE_FOLDER)
        proj_src = os.path.join(config.PROJECT_PATH_SCHEMA_UPDATE_FOLDER, src_name)
        proj_dst = os.path.join(config.PROJECT_PATH_SCHEMA_UPDATE_FOLDER, dst_name)
        file_src = os.path.join(update_folder_path, src_name)
        file_dst = os.path.join(update_folder_path, dst_name)
        res = self.project_file.get_res(proj_src)
        if res is not None:
            git_mv(file_src, file_dst, cwd=config.BASE_DIR)
            self.project_file.rename(proj_src, proj_dst)
        else:
            raise Exception("[" + proj_src + "] is not a resource in project")

    @staticmethod
    def __update_current_version_files(u_num, c_num, m_num):
        file_path = os.path.join(config.BASE_DIR, config.PATH_CURRENT_VERSION_TXT)
        with open(file_path, 'w') as f:
            f.write("{0}\n{1}\n{2}".format(u_num, c_num, m_num))



import config
import git
from msql.fixschema import FixSQLSchema
from msql.options import get_opt
from msql.project import ProjectFile
from msql.rename import RenameBranchSQLFiles

if __name__ == "__main__":
    try:
        baseDir = get_opt()
        config.BASE_DIR = baseDir
        print("Rename SQL Files In Folder: [" + baseDir + "]")

        project = ProjectFile()
        print("Load DataLayer Project File")
        project.load()

        fix_schema = FixSQLSchema()
        print("Fix SCHEMA in Update SQLs")
        fix_schema.fix()

        re_sqls = RenameBranchSQLFiles(project)
        print("Rename Branch SQL Files")
        re_sqls.rename_branch_sql_files()

        print("End")

    except Exception:
        print("Get Exception, So Reset Git Repo.")
        git.git_reset(hard=True, cwd=config.BASE_DIR)
        raise

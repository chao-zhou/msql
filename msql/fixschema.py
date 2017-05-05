import re

from msql import sqlfiles
from msql.pattern import *


class FixSQLSchema:
    def __init__(self):
        self.regex = re.compile("s_dev.", re.IGNORECASE)

    def fix(self):
        for f in sqlfiles.get_branch_sql_files(UPDATE_SQL_FILE_PATTERN.branch_search_pattern):
            content = self._read_file(f)
            if content is None:
                return
            content2, count = self.regex.subn("[SCHEMA].", content)
            if count > 0:
                self._write_file(content2)

    @staticmethod
    def _read_file(path):
        try:
            with open(path, 'rt', encoding="utf8") as f:
                content = f.read()
            f.close()
            return content
        except Exception:
            return None

    @staticmethod
    def _write_file(path, content):
        with open(path, 'wt', encoding="utf8") as f:
            f.write(content)
        f.close()

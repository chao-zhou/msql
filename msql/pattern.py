METRIC_SQL_SEARCH_PATTERN = "Metrics_SQL_*.sql"
CONVERSION_SQL_SEARCH_PATTERN = "Conversion_SQL_*.sql"
UPDATE_SQL_SEARCH_PATTERN = "SQL_*.sql"

METRIC_BRANCH_SQL_SEARCH_PATTERN = "Metrics_SQL_*_*.sql"
CONVERSION_BRANCH_SQL_SEARCH_PATTERN = "Conversion_SQL_*_*.sql"
UPDATE_BRANCH_SQL_SEARCH_PATTERN = "SQL_*_*.sql"

METRIC_SQL_FILE_FORMAT = "Metrics_SQL_{}.sql"
CONVERSION_SQL_FILE_FORMAT = "Conversion_SQL_{}.sql"
UPDATE_SQL_FILE_FORMAT = "SQL_{}.sql"


class SQLFilePattern:
    def __init__(self, search_pattern, branch_search_pattern, output_file_format):
        self.search_pattern = search_pattern
        self.branch_search_pattern = branch_search_pattern
        self.output_file_format = output_file_format


METRIC_SQL_FILE_PATTERN = SQLFilePattern(METRIC_SQL_SEARCH_PATTERN, METRIC_BRANCH_SQL_SEARCH_PATTERN,
                                         METRIC_SQL_FILE_FORMAT)
CONVERSION_SQL_FILE_PATTERN = SQLFilePattern(CONVERSION_SQL_SEARCH_PATTERN, CONVERSION_BRANCH_SQL_SEARCH_PATTERN,
                                             CONVERSION_SQL_FILE_FORMAT)
UPDATE_SQL_FILE_PATTERN = SQLFilePattern(UPDATE_SQL_SEARCH_PATTERN, UPDATE_BRANCH_SQL_SEARCH_PATTERN,
                                         UPDATE_SQL_FILE_FORMAT)

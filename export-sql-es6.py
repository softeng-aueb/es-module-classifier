from regex import regexes_cjs, regexes_amd, regexes_import, regexes_export

def regex_contains(exp, shouldMatch):
    return f" REGEXP_CONTAINS(content, r{repr(exp)}) = {'true' if shouldMatch else 'false'} "

def getBigQueryStmts(regexes, shouldMatch, shouldMatchAny):
    stmt = ""
    sep = " OR \n" if shouldMatchAny else " AND \n"
    bq_exprs = map(lambda exp: regex_contains(exp, shouldMatch), regexes)
    stmt = sep.join(bq_exprs).replace("\\\\", "\\")
    return stmt

print('---------------- ES6 conditions ------------------------- ')

bq_stmt = getBigQueryStmts(regexes_import + regexes_export, True, True)
print(bq_stmt)

print('----------------- AMD conditions --------------------------')
bq_stmt = getBigQueryStmts(regexes_amd, True, True)
print(bq_stmt)

print('----------------- CJS conditions --------------------------')
bq_stmt = getBigQueryStmts(regexes_cjs, True, True)
print(bq_stmt)

    
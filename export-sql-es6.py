from regex import regexes_cjs, regexes_amd, regexes_import, regexes_export

def regex_contains(exp, shouldMatch):
    return f" REGEXP_CONTAINS(content, r'{exp}') = {'true' if shouldMatch else 'false'} "

def getBigQueryStmts(regexes, shouldMatch, shouldMatchAny):
    bq_expr = map(lambda exp: regex_contains(exp, shouldMatch), regexes)
    if shouldMatchAny:
        return " OR \n".join(bq_expr)
    else:
        return " AND \n".join(bq_expr)

print('---------------- ES6 conditions ------------------------- ')

bq_stmt = getBigQueryStmts(regexes_import + regexes_export, True, True)
print(bq_stmt)

print('----------------- AMD conditions --------------------------')
bq_stmt = getBigQueryStmts(regexes_amd, True, True)
print(bq_stmt)

print('----------------- CJS conditions --------------------------')
bq_stmt = getBigQueryStmts(regexes_cjs, True, True)
print(bq_stmt)

    
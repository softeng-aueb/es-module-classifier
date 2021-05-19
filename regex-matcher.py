import re2
from es6_benchmarks import es6_imports, es6_exports

regexes_cjs = [
    '^\s*(define\s*\( | require\s*\(\s*\[ | requirejs\s*\()',
    '^\s*(exports\s*[.|=] | module\.exports\s*[.|=] | require\s*\()'
]

regexes_import = [
    '^\s*import\s+[a-zA-Z_][a-zA-Z0-9_]*\s*from\s+',
    '^\s*import\s+\*\s+as\s+',
    '^\s*import\s+.*{.*}\s*from\s+',
    '^\s*import\s+[a-zA-Z_][a-zA-Z0-9_]*,\s*\*\s*as\s+.*from\s+',
    '^\s*import\s*((\".*\")|(\'.*\'))',
]

regexes_export = [
    '^\s*export\s*(let|var|const)\s*[a-zA-Z_][a-zA-Z0-9_]*[,\s]\s*',
    '^\s*export\s*(default)?\s*function\s*([a-zA-Z_][a-zA-Z0-9_]*)?\s*\(.*',
    '^\s*export\s*(default)?\s*class\s*[a-zA-Z_][a-zA-Z0-9_]*\s*[\{$]',
    '^\s*export\s*(const)?\s*\{\s*([a-zA-Z_][a-zA-Z0-9_]*|\}|$)',
    '^\s*export\s*default\s*([a-zA-Z_][a-zA-Z0-9_]*|\( |\{|[0-9\-])',
    #'^((\s*)export(\s*)\*)'
]

def assertMatches(regexList, content):
    matches = False
    for regex in regexList:
        r = re2.findall(regex, content, re2.MULTILINE)
        if (len(r) > 0):
            #print(content)
            print('Matches', regex)
            matches = True
            break
    return matches

def assertNotMatches(regexList, content):
    notMatches = False
    for regex in regexList:
        r = re2.findall(regex, content, re2.MULTILINE)
        if (len(r) == 0):
            print('! Matches', regex)
            notMatches = True
            break
    return notMatches

def test_regexes(regexes, snippets, nomatch_regexes, test_name):
    test_count = 0
    error_count = 0
    for snippet in snippets:
        print('-------------------------')
        test_count+=1
        shouldMatch = snippet[1]
        if shouldMatch:
            res = assertMatches(regexes, snippet[0])
            if not(res):
                error_count+=1
                print(test_name, 'regexes failed for \n', snippet)
        else:
            res = assertNotMatches(regexes, snippet[0])
            if not(res):
                error_count+=1
                print(test_name, 'regexes succeeded for \n', snippet)
        if len(nomatch_regexes) > 0:
            test_count+=1
            res = assertNotMatches(nomatch_regexes, snippet[0])
            if not(res):
                error_count+=1
                print(test_name, 'regexes succeeded for \n', snippet)
    print(test_name, 'regexes ', error_count, '/', test_count, 'tests failed')

test_regexes(regexes_import, es6_imports, regexes_cjs, 'Import')
test_regexes(regexes_export, es6_exports, regexes_cjs, 'Export')




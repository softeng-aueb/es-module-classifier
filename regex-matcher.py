import re2
from es6_benchmarks import es6_imports, es6_exports
from regex import regexes_cjs, regexes_import, regexes_export


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
    notMatches = True
    for regex in regexList:
        r = re2.findall(regex, content, re2.MULTILINE)
        if (len(r) > 0):
            print('! Matches', regex)
            notMatches = False
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




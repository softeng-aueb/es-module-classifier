import re2
from es6_benchmarks import es6_tests

regexes_cjs = [
    '(?s)define\( | require\(\[ | requirejs\(',
    '(?s)exports[.|=] | module\.exports[.|=] | require\('
]

regexes_import = [
    '^[\s]*import[\s]*[a-zA-Z_][a-zA-Z0-9_]*[\s]*from[\s]+',
    '^[\s]*import[\s]+\*[\s]+as[\s]+',
    '^[\s]*import.*[\s]*{.*}[\s]*from[\s]+',
    '^((\s*)import(\s*)[a-zA-Z]+(\s*),(\s*)\*)',
    '^((\s*)import(\s*)\")',
]

regexes_export = [
    '^((\s*)export(\s*) let|(\s*)export(\s*) var|(\s*)export(\s*) const)',
    '^((\s*)export(\s*)function)',
    '^((\s*)export(\s*)class)',
    '^((\s*)export(\s*){)',
    '^((\s*)export(\s*)default)',
    '^((\s*)export(\s*)\*)'
]

def assertMatches(regexList, content):
    matches = False
    for regex in regexList:
        r = re2.findall(regex, content)
        if (len(r) > 0):
            #print(content)
            print('Matches', regex)
            matches = True
            break
    return matches

def assertNotMatches(regexList, content):
    notMatches = False
    for regex in regexList:
        r = re2.findall(regex, content)
        if (len(r) == 0):
            print('! Matches', regex)
            notMatches = True
            break
    return notMatches


for snippet in es6_tests:
    shouldMatch = snippet[1]
    if shouldMatch:
        res = assertMatches(regexes_import, snippet[0])
        if not(res):
            print('Import regexes failed for \n', snippet)
    else:
        res = assertNotMatches(regexes_import, snippet[0])
        if not(res):
            print('Import regexes succeeded for \n', snippet)




# for regex in regexes_import:
#     r = re2.findall(regex, contents)
#     if (len(r) >= 0):
#         print(regex, ':', 'PASS')
#     else:
#         print(regex, ':', 'FAIL')






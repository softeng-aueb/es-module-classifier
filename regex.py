regexes_cjs = [
    '(^|\n)\s*((let|var|const)?\s*[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*)?require\s*\(',
    '(^|\n)\s*((let|var|const)?\s*[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*)?(exports\s*[.|=]|module\.exports\s*[.|=])'
]

regexes_amd = [
    '(^|\n)\s*(require\s*\(\s*\[|requirejs\s*\()',
    '(^|\n)\s*define\s*\(\s*(function\s*|\[?\s*[\'\"])'
]

regexes_import = [
    '(^|\n)\s*import\s+[a-zA-Z_][a-zA-Z0-9_]*\s*from\s+',
    '(^|\n)\s*import\s+\*\s+as\s+',
    '(^|\n)\s*import\s+.*{.*}\s*from\s+',
    '(^|\n)\s*import\s+[a-zA-Z_][a-zA-Z0-9_]*,\s*\*\s*as\s+.*from\s+',
    '(^|\n)\s*import\s*((\".*\")|(\'.*\'))',
]

regexes_export = [
    '(^|\n)\s*export\s*(let|var|const)\s*[a-zA-Z_][a-zA-Z0-9_]*[,\s]\s*',
    '(^|\n)\s*export\s*(default)?\s*function\s*([a-zA-Z_][a-zA-Z0-9_]*)?\s*\(.*',
    '(^|\n)\s*export\s*(default)?\s*class\s*[a-zA-Z_][a-zA-Z0-9_]*\s*[\{$]',
    '(^|\n)\s*export\s*(const)?\s*\{\s*([a-zA-Z_][a-zA-Z0-9_]*|\}|$)',
    '(^|\n)\s*export\s*default\s*([a-zA-Z_][a-zA-Z0-9_]*|\(|\{|[0-9\-])',
    '(^|\n)\s*export\s*\*\s*(as\s*[a-zA-Z_][a-zA-Z0-9_]*\s*)?from\s*'
]

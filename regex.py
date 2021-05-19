regexes_cjs = [
    '^\s*((let|var|const)?\s*[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*)?require\s*\(',
    '^\s*((let|var|const)?\s*[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*)?(exports\s*[.|=]|module\.exports\s*[.|=])'
]

regexes_amd = [
    '^\s*(require\s*\(\s*\[|requirejs\s*\()',
    '^\s*define\s*\(\s*(function\s*|\[?\s*[\'\"])'
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
    '^\s*export\s*default\s*([a-zA-Z_][a-zA-Z0-9_]*|\(|\{|[0-9\-])',
    '^\s*export\s*\*\s*(as\s*[a-zA-Z_][a-zA-Z0-9_]*\s*)?from\s*'
]

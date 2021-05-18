
es6_tests = [
#### default import
["""import _default_123Export from "module-name";

_default_123Export.require('abc')
""", True],

["""
    import _default_123Export from "module-name";

_default_123Export.require('abc')
""", True],

#### import * from
["""import   *  as  name  from "module-name";

    name.define(['a','b'])
""", True],

#### Named imports
["""import { export1 } from "module-name";
console.log(export1)
    export1.require('x')

""", True],

["""import { export1,export2 as alias}from "module-name";
console.log(export1)
    export1.require('x')

""", True],

["""
    import defaultExport, { export1 [ , [...] ] } from "module-name";

    console.log(defaultExport)
""", True],

#### Default and * import 
["""import defaultExport, * as name from "module-name";

console.log(defaultExport)
""", True],

["""   import   *  as  name, defaultExport from "module-name";

console.log(defaultExport)
""", True],

#### import for side effects
["""
import "module-name";
""", True],

["""
import 'module-name';
""", True],

["""import export1 } from "module-name";""", False]

]



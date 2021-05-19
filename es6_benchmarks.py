
es6_imports = [
#### default import
["""
// this is a module
import _default_123Export from "module-name";
// define an appropriate module
_default_123Export.require('abc')

""", True],

["""
    import _default_123Export from "module-name";

_default_123Export.require('abc')
""", True],

#### import * from
["""import   *  as  name  from "module-name";
// export appropriate modules
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

["""import export1 } from "module-name";""", False],
]

es6_exports = [
#### export declarations
["""
import { export1 } from "module-name
// define an appropriate module
export let name1, name2, nameN;
// module.exports""", True],

["""export a variable""", False],

["""
// define an appropriate module
export const name1, name2, nameN;
// module.exports""", True],

["""
import { export1 } from "module-name
// define an appropriate module
export var name1, name2, nameN;
// module.exports""", True],

#### Export classes functions
["""
import { export1 } from "module-name
// define an appropriate module
export function function123_Name(var1){
    console.log('hello')
}
// module.exports""", True],

["""
import { export1 } from "module-name
// define an appropriate module
    export function   (var1){
    console.log('hello')
}
// module.exports""", True],

["""export function that does this job (of course right)""", 
False],

["""export class ClassName123 {...}

// module.exports""", True],

["""export class _ClassName123 
{}

// module.exports""", True],

["""export class class1 class2 {...}""", False],

#### Export list
["""
export { name1, name2, …, nameN };
// module.exports""", True],
["""
export {   
     name1, name2, …, nameN };
// module.exports""", True],
["""
export {   }
// module.exports""", True],

#### Renaming exports
["""
export { variable1 as name1, variable2 as name2, …, nameN };
// module.exports""", True],

#### Export destructured assignments with destructuring
["""
export const { name1, name2: bar } = o;
// module.exports""", True],

#### Default exports
["""
export default expression;
// module.exports""", True],

["""
export default function (…) { … } // also class, function*
// module.exports""", True],

["""
export default function name1(…) { … } // also class, function*
// module.exports""", True],

["""
export default class name_class{
}
obj.define([lodash])
//module.exports""", True],

["""
export { name1 as default, … };
obj.define([lodash])
//module.exports""", True],

#### Aggregating modules
["""
export * from './utils.js' //
obj.define([lodash])
//module.exports""", True],

["""
export * as name1 from './utils.js' //
obj.define([lodash])
//module.exports""", True],

["""
export { name1, name2, nameN } from './utils.js' //
obj.define([lodash])
//module.exports""", True],

["""
export { import1 as name1, import2 as name2, …, nameN } from './utils.js' //
obj.define([lodash])
//module.exports""", True],

["""
export { default, name1 } from './utils.js' //
obj.define([lodash])
//module.exports""", True],

]

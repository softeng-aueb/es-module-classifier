
cjs = [
#### require module

["""var bodyParser = require('body-parser')
var EventEmitter = require('events').EventEmitter;
""", True],

["""
let bodyParser = require('body-parser')
console.log('hello')
""", True],

["""const bodyParser = require('body-parser')

console.log('hello')
""", True],

["""bodyParser = require('body-parser')

console.log('hello')
""", True],

["""
 require('body-parser')
//define(['lodash'], function(){})
console.log('hello')
""", True],

["""
// you should require a module
""", False],

["""
a.require('body-parser')
// do not use require()
""", False],


#### module exports

["""
module.exports = Route;
console.log('hello')
""", True],

["""
exports = Route;
console.log('hello')
""", True],

["""
exports = module.exports = createApplication;
console.log('hello')
""", True],

["""
exports.Route = Route;
exports.Router = Router;
""", True],

["""
module.exports.Route = Route;
module.exports.Router = Router;
""", True],


["""
var proto = module.exports = function(options) {
  var opts = options || {};

  }
""", True],

["""
module.exports.dot = function (modules, circular, config) {
	const options = createGraphvizOptions(config);
""", True],


["""
// it exports everything
a.exports.property = 10
var x = exports('hello')

""", False],

]

amd = [

["""
define(['amd-loader'], function(amdLoader) {
  var cjsRequireRegExp = /\s*require\s*\(\s*["']([^'"\s]+)["']\s*\)/g;
}
""", True],

["""
define([
	"../_base/lang", "../_base/declare", "../Deferred", "../_base/array",
	"./util/QueryResults", "./util/SimpleQueryEngine" /*=====, "./api/Store" =====*/
], function(lang, declare, Deferred, array, QueryResults, SimpleQueryEngine /*=====, Store =====*/){

""", True],

["""
define(function (require, exports, module) {
    "use strict";

require("utils/Global");
var EventDispatcher = require("utils/EventDispatcher");
""", True],

["""
define(function (require, exports, module) {
    "use strict";

    var AppInit             = require("utils/AppInit"),
        Commands            = require("command/Commands"),
""", True],


["""
a.define(varname)
a.require(name1)
a.requirejs(name2)
var x = define(y)
define(abc)
dojo.require('dojo.cookie');
xdomainExecSequence.push('local1-3');
""", False],

]


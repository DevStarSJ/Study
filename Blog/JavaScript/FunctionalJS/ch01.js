var _ = require('underscore');

function splat(fun) {
    return function(array) {
        return fun.apply(null, array);
    };
}

var addArrayElements = splat(function(x, y) { return x+y });

console.log(addArrayElements([1, 2]));

function unsplat(fun) {
    return function() {
        return fun.call(null, _.toArray(arguments));
    };
}

var joinElements = unsplat(function(array) { return array.join(' ')});

console.log(joinElements(1,2));
console.log(joinElements('-','$','/','!',':'));

function fail(thing) {
    throw new Error(thing);
}

function warn(thing) {
    console.log(["WARNING:",thing].join(' '));
}

function note(thing) {
    console.log(["NOTE:", thing].join(' '));
}

function parseAge(age) {
    if (!_.isString(age)) fail("Expection a string");

    var a;

    note("Attempong to parse an age");

    a = parseInt(age, 10);

    if (_.isNaN(a)) {
        warn(["Could not parse age:", age].join(' '));
        a = 0;
    }

    return a;
}

console.log(parseAge("42"));
//parseAge(42);
console.log(parseAge("Flog"));

function isIndexed(data) {
    return _.isArray(data) || _.isString(data);
}

function nth(a, index) {
    if (!_.isNumber(index)) fail("Expected a number as the index");
    if (!isIndexed(a)) fail("Not supported on non-indexed type");
    if (index < 0 || index > a.length - 1)
        fail("Index value is out of bounds");

    return a[index];
}

letters = ['a','b','c'];
console.log(nth(letters,1));
console.log(nth('abcd',0));

function compareLessThanOrEqual(x, y) {
    if (x < y) return -1;
    if (y < x) return 1;
    return 0;
}

console.log([2,3,-1,-6,0,-108,42,10].sort(compareLessThanOrEqual));

function lessOrEqual(x, y) {
    return x <= y;
}

console.log([2,3,-1,-6,0,-108,42,10].sort(lessOrEqual));

function existy(x) {
    return x != null;
}

function truthy(x) {
    return x != false && existy(x);
}

function comparator(pred) {
    return function(x, y) {
        if (truthy(pred(x,y)))
            return -1;
        else if (truthy(pred(y,x)))
            return 1;
        else
            return 0;
    }
}

console.log([2,3,-1,-6,0,-108,42,10].sort(comparator(lessOrEqual)));

function lameCSV(str) {
    return _.reduce(str.split("\n"),  function(table, row) {
        table.push(_.map(row.split(","), function(c) { return c.trim()}));
        return table;
    }, []);
}

var peopleTable = lameCSV("name,age,hair\nMerble,35,red\nBob,64,blonde");

console.log(peopleTable);



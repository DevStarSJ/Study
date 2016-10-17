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

function parseAge(age) {
    if (!_.isString(age)) throw new Error("Expection a string");
    var a;

    console.log("Attempong to parse an age");

    a = parseInt(age, 10);

    if (_.isNaN(a)) {
        console.log(["Could not parse age:", age].join(' '));
        a = 0;
    }

    return a;
}

console.log(parseAge("42"));
//parseAge(42);
console.log(parseAge("Flog"));
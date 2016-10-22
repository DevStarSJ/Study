// https://github.com/marpple/abc-functional-javascript/wiki

var log = console.log


function badd(a) {
    return function(b) {
        return a+b;
    }
}

log(badd(10)(5))

var add5 = badd(5)
log(add5(3))

function filter(list, predicate) {
    var new_list = []
    for (var i = 0, len = list.length; i < len; i++) {
        if (predicate(list[i]))
            new_list.push(list[i])
    }
    return new_list
}

function map(list, iteratee) {
    var new_list = [];
    for (var i = 0, len = list.length; i < len; i++) {
        new_list.push(iteratee(list[i]))
    }
    return new_list
}

var users = [
    { id: 1, name: "CJ", age: 32 },
    { id: 2, name: "HA", age: 25 },
    { id: 3, name: "BJ", age: 32 },
    { id: 4, name: "PJ", age: 28 },
    { id: 5, name: "JE", age: 27 },
    { id: 6, name: "JM", age: 32 },
    { id: 7, name: "HI", age: 24 }
];

var temp_users = [];
log(
    filter(users, function(user) { return user.age < 30})
        .length
)

log(
    filter(users, (user) => { return user.age >= 30 })
)

function log_length(value) {
    log(value.length)
    return value
}

log(
    log_length(
        map(
            filter(users, (user) => { return user.age < 30}),
            (user) => { return user.age }
        )
    )
)

function bvalue(key) {
    return (obj) => { return obj[key] }
}

log(bvalue('a')({a: 'hi'}))

log(
    log_length(
        map(
            filter(users, user => user.age < 30),
            bvalue('age')
        )
    )
)





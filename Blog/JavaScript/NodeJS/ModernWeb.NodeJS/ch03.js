/**
 * Created by seokjoonyun on 2016. 10. 5..
 */
console.log('filename: %s', __filename);
console.log('dirname: %s', __dirname);

console.log('JSON : %j', {name : 'Luna'});

console.time('alpha');

var output = 1
for (var i = 1; i < 10000; i++) {
    output += i;
}
console.log('sum of 10000 : %d', output);
console.timeEnd('alpha');

console.log('- process.');
console.log('  - env :', process.env);
console.log('  - version :', process.version);
console.log('  - versions :', process.versions);
console.log('  - arch :', process.arch);
console.log('  - platform : ', process.platform);
console.log('  - memoryUsage() :', process.memoryUsage());
console.log('  - process.uptime():', process.uptime());

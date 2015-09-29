/* jshint node: true */

'use strict';

var gulp = require('gulp');
var less = require('gulp-less');
var concat = require('gulp-concat');
// var watch = require('gulp-watch');
var path = require('path');
var eventStream = require('event-stream');


var LESS_SRC = '/app-client/src/css/*.less';
var CSS_SRC = '/app-client/src/**/*.css';
var CSS_DEST = '/app-client/build/css/';



gulp.task('css', function() {

  var css1 = gulp.src(CSS_SRC);

  var css2 = gulp.src(LESS_SRC)
    .pipe(less({
      paths: [ path.join(__dirname, 'less', 'includes') ]
    }));

  eventStream.merge(css1, css2)
    .pipe(concat('bundle.css'))
    .pipe(gulp.dest(CSS_DEST));
});



/* BUILD */

gulp.task('build', ['css'], function () {


});

/* DEV WATCH */

gulp.task('watch', ['build'], function () {

  gulp.watch([LESS_SRC, CSS_SRC], ['css']);


});

var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var livereload = require('gulp-livereload');

gulp.task('sass', function() {
    return gulp.src('assets/styles/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('static/css'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('static/css'))
        .pipe(livereload());
});

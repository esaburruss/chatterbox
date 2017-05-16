var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var livereload = require('gulp-livereload');
var connect = require('gulp-connect');

gulp.task('connect', function(){
  connect.server({
    root: 'public',
    livereload: true
  });
});

gulp.task('sass', function() {
    return gulp.src('assets/styles/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('static/css'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('static/css'))
        .pipe(livereload());
});

gulp.task('livereload', function (){
  gulp.src('./static/**/*')
  .pipe(connect.reload());
});

gulp.task('watch', function () {
  gulp.watch('./assets/styles/*.scss', ['sass']);
  gulp.watch('./static/**/*', ['livereload']);
});

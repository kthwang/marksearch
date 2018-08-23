var gulp = require('gulp');
var gulpFilter = require('gulp-filter');
var fs = require('fs');
$ = require('gulp-load-plugins')();
var argv = require('yargs').argv;
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var minifyCSS = require('gulp-minify-css');
var sass = require('gulp-sass');
var cssnano = require('gulp-cssnano');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('autoprefixer');
var postcss = require('gulp-postcss');

// COMPILE BOOTSTRAP FILES
gulp.task('bootstrap', function() {
  return gulp.src('sass/bootstrap/bootstrap.scss')
    .pipe(sourcemaps.init())
    .pipe(sourcemaps.write())
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sass({
      includePaths: ['sass/bootstrap']
    }))
    .pipe(postcss([autoprefixer()]))
    .pipe(gulp.dest('../dist/assets/css/vendor'))
    .pipe(rename('bootstrap.css'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('../dist/assets/css/vendor'));
});
// CREATE SASS MAIN BUNDLE FILES
gulp.task('sass', function() {
  return gulp.src('sass/common/main.scss')
    .pipe(sourcemaps.init())
    .pipe(sourcemaps.write())
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sass({
      includePaths: ['sass']
    }))
    .pipe(postcss([autoprefixer()]))
    .pipe(gulp.dest('../dist/assets/css/common'))
    .pipe(rename('main.bundle.css'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('../dist/assets/css/common'));
});
// CREATE DEMO VERTICAL BUNDLE FILES
gulp.task('verticalLayout', function() {
  return gulp.src('sass/layouts/vertical/core/*')
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sass({
      includePaths: ['sass/layouts/vertical/core']
    }))
    .pipe(gulp.dest('../dist/assets/css/layouts/vertical/core'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('../dist/assets/css/layouts/vertical/core'));
});
// CREATE DEMO HORIZONTAL BUNDLE FILES
gulp.task('horizontalLayout', function() {
  return gulp.src('sass/layouts/horizontal/core/*')
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sass({
      includePaths: ['sass/layouts/horizontal/core']
    }))
    .pipe(gulp.dest('../dist/assets/css/layouts/horizontal/core'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('../dist/assets/css/layouts/horizontal/core'));
});
// CREATE BUNDLES FOR VERTICAL MENU TYPES
gulp.task('verticalLayoutMenu', function() {
  return gulp.src('sass/layouts/vertical/menu-type/*')
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sass({
      includePaths: ['sass/layouts/vertical/menu-type']
    }))
    .pipe(gulp.dest('../dist/assets/css/layouts/vertical/menu-type'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('../dist/assets/css/layouts/vertical/menu-type'));
});
// CREATE BUNDLES FOR HORIZONTAL MENU TYPES
gulp.task('horizontalLayoutMenu', function() {
  return gulp.src('sass/layouts/horizontal/menu-type/*')
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sass({
      includePaths: ['sass/layouts/horizontal/menu-type']
    }))
    .pipe(gulp.dest('../dist/assets/css/layouts/horizontal/menu-type'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('../dist/assets/css/layouts/horizontal/menu-type'));
});
// CREATE THEME FILES FOR VERTICAL LAYOUT
gulp.task('verticalThemes', function() {
  return gulp.src('sass/layouts/vertical/themes/*')
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sass({
      includePaths: ['sass/layouts/vertical/themes']
    }))
    .pipe(gulp.dest('../dist/assets/css/layouts/vertical/themes'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('../dist/assets/css/layouts/vertical/themes'));
});
// CREATE THEME FILES FOR HORIZONTAL LAYOUT
gulp.task('horizontalThemes', function() {
  return gulp.src('sass/layouts/horizontal/themes/*')
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sass({
      includePaths: ['sass/layouts/horizontal/themes']
    }))
    .pipe(gulp.dest('../dist/assets/css/layouts/horizontal/themes'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('../dist/assets/css/layouts/horizontal/themes'));
});
//ADD WATCH
gulp.task('watch', function() {
  gulp.watch('sass/**/*.scss', ['bootstrap','sass', 'verticalLayout','horizontalLayout','verticalLayoutMenu','horizontalLayoutMenu','verticalThemes','horizontalThemes']);
});

//ERROR HANDELING
function errorAlert(err) {
  console.log(err.toString());
  this.emit("end");
}

gulp.task('default', ['bootstrap','sass','verticalLayout', 'horizontalLayout','verticalLayoutMenu','horizontalLayoutMenu','verticalThemes','horizontalThemes','watch']);

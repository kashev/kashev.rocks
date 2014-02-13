/*
  Kashev Dalmia
  kashev.dalmia@gmail.com

  kashevdalmia.com

  Gruntfile.js
*/

/* GRUNT CONFIGURATION */
module.exports = function(grunt) {
  var html_files = {
    'dist/index.html' : 'src/index.html'
  };
  var css_files  = {
    'dist/css/main.css' : 'src/css/main.scss'
  };
  var js_files   = {
    'dist/js/main.js' : 'src/js/main.js'
  };
  
  var img_copy =  {
    flatten : true,
    expand : true,
    cwd: 'src/img',
    src: ['**/*'],
    dest: 'dist/img/'
  };

  grunt.initConfig({
    connect: {
      server: {
        options: {
          base : 'dist',
          livereload : true,
        },
      }
    },
    // JS Hint Options
    jshint: {                                  // task
      src: ['Gruntfile.js', 'src/js/main.js'],
      options: {
        curly : true,
        eqeqeq : true,
        immed : true,
        latedef : true,
        newcap : true,
        noarg : true,
        sub : true,
        undef : true,
        boss : true,
        eqnull : true,
        browser : true,
        globals : {
          require : true,
          define : true,
          requirejs : true,
          describe : true,
          expect : true,
          it : true,
          module  : true
        }
      }
    },
    // Sass options
    sass: {                              // Task
      dev : {                            // Target
        options : {                      // Target options
          style : 'expanded',
          trace : true,
          unixNewlines : true
        },
        files : css_files
      },
      dist : {
        options : {
          style : 'compressed',
          trace : true,
          unixNewlines : true
        },
        files : css_files
      }
    },
    // copy options
    copy : {
      dev : {
        files: [
          html_files,
          js_files,
          img_copy
        ]
      },
      dist : {
        files: [
          img_copy
        ]
      }
    },
    // htmlmin - for dist
    htmlmin : {
      dist : {
        options : {
          removeComments: true,
          collapseWhitespace: true
        },
        files : html_files
      }
    },
    // uglify - for dist
    uglify : {
      dist : {
        files : js_files,
        options : {
          mangle : false,

        }
      }
    },
    watch : {
      options : {
        livereload : true,
      },
      html : {
        files : ['src/index.html'],
        tasks : ['copy:dev'],
      },
      js : {
        files : ['src/js/*.js'],
        tasks : ['jshint', 'copy:dev'],
      },
      css : {
        files : ['src/css/main.scss'],
        tasks : ['sass:dev'],
      },
      grunt : {
        files : ['Gruntfile.js'],
        tasks : ['jshint', 'copy:dev'],
      }
    }
  });

  /* Load Tasks */
  // Load JSHint Task
  grunt.loadNpmTasks('grunt-contrib-jshint');
  // Load Sass Compilation Task
  grunt.loadNpmTasks('grunt-contrib-sass');
  // Load Copy Tasks
  grunt.loadNpmTasks('grunt-contrib-copy');
  // Load Grunt Connect
  grunt.loadNpmTasks('grunt-contrib-connect');
  // Load Grunt Watch
  grunt.loadNpmTasks('grunt-contrib-watch');
  /* DIST ONLY TASKS */
  // Load HTML Minification Task
  grunt.loadNpmTasks('grunt-contrib-htmlmin');
  // Load JS Minification Task
  grunt.loadNpmTasks('grunt-contrib-uglify');


  // Default task is dev. dist builds deploy folder.
  grunt.registerTask('default', [
    'jshint',
    'sass:dev',
    'copy:dev'
  ]);
  
  grunt.registerTask('dist', [
    'jshint',
    'sass:dist',
    'htmlmin',
    'uglify',
    'copy:dist'
  ]);

  grunt.registerTask('server', [
    'jshint',
    'sass:dev',
    'copy:dev',
    'connect',
    'watch'
  ]);

};

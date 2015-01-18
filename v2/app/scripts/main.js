'use strict'

function MainCtrl () {
    this.someObject = 'azerty'
    this.doSomething = function () {
    };
}

angular
.module('MyPage', [])
.controller('MainCtrl', MainCtrl)
.config(function( $routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'main.html'
    })
    .when('/tags/:tagId', {
      templateUrl: 'partials/template2.html'
    })
    .when('/another', {
      templateUrl: 'partials/template1.html'
    })
    .otherwise({ redirectTo: '/' });
})

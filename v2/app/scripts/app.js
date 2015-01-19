'use strict'

function MainCtrl () {
    this.someObject = 'azerty'
    this.doSomething = function () {
    };
}

angular
.module('MyPage', ['ngRoute'])
.controller('MainCtrl', MainCtrl)
.config(['$routeProvider', function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl: 'views/main.html'
    })
    .when('/about', {
        templateUrl: 'views/about.html'
    })
    .otherwise({redirectTo: '/'});
}]);
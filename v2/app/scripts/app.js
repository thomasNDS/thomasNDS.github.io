'use strict'

//////////////////////////////////////CONTROLLER///////////////////////////////
function MainCtrl () {
    this.someObject = 'azerty'
    this.doSomething = function () {
    };
}

function LangCtrl ($translate) {
    this.lang = $translate.storage()
    console.log(this.lang)

    this.switchLang = function(lang){
        $translate.use(lang)
        window.localStorage['lang'] = lang
    }
}

//////////////////////////////////////APP DEFINITION///////////////////////////////
angular
.module('MyPage', ['ngRoute', 'pascalprecht.translate'])
.controller('MainCtrl', MainCtrl)
.controller('LangCtrl', LangCtrl)
.config(['$routeProvider','$translateProvider', function($routeProvider, $translateProvider) {
    console.log($translateProvider)
    $routeProvider
    .when('/', {
        templateUrl: function(attr){
            return 'views/main.html'
        }
    })
    .when('/about', {
        templateUrl: function(attr){
            return 'views/about.html'
        }
    })
    .otherwise({redirectTo: '/'});

    //////language settings//////
    $translateProvider
    .translations('fr', translationsFR)
    .translations('en', translationsEN)
    .fallbackLanguage('en');
    if (window.localStorage['lang']){
        //language save
        $translateProvider.use(window.localStorage['lang'])
    }else{
        //determine language
        $translateProvider.determinePreferredLanguage()
    }

}]);
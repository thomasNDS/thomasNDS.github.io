'use strict'

//////////////////////////////////////CONTROLLER///////////////////////////////
function MainCtrl () {
    this.someObject = 'azerty'
    this.doSomething = function () {
    };
}

function LangCtrl ($translate) {
    this.lang = $translate.storage()

    this.switchLang = function(lang){
        $translate.use(lang)
        window.localStorage['lang'] = lang
    }
}
LangCtrl.$inject = ['$translate']

////////////////////////////////// APP DEFINITION ///////////////////////////////
angular
    .module('MyPage', ['ngRoute', 'pascalprecht.translate','ngAnimate'])
    .controller('MainCtrl', MainCtrl)
    .controller('LangCtrl', LangCtrl)
    .config(['$routeProvider','$translateProvider', function($routeProvider, $translateProvider) {
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
            .when('/mit', {
            templateUrl: function(attr){
                return 'views/MIT.html'
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
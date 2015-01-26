'use strict'

//////////////////////////////////////TRANSLATIONS///////////////////////////////
var translationsEN = {
    en: 'en',
    languages: 'Languages',
    Settings: 'Settings',
    addYourWeight: 'Add your weight',
    validWeight: 'You need to a valid weight.',
}

var translationsFR = {
    en : 'fr',
    languages : 'Langues',
    Settings : 'Paramètres',
    addYourWeight : 'Ajouter son poids',
    validWeight: 'Vous devez rentrer un poids valide.',
}

//////////////////////////////////////CONTROLLER///////////////////////////////
function MainCtrl () {
    this.someObject = 'azerty'
    this.doSomething = function () {
    };
}

function LangCtrl ($translate) {
    this.lang = $translate.storage()
  console.log(this.lang)
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
            if (attr.lang !== 'fr') attr.lang = 'en'
            return 'views/' + attr.lang + '/main.html'
        }
    })
    .when('/:lang/about/', {
        templateUrl: function(attr){
            if (attr.lang !== 'fr') attr.lang = 'en'
            return 'views/' + attr.lang + '/about.html'
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
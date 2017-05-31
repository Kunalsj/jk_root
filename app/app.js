  var app = angular.module("app", [])
    .controller("CustomDirectiveController", function ($scope) {
        $scope.username = "Someone";
        $scope.address = "Someplace";
    });

    app.directive('myCustomUrl', function () {
        return {
            templateUrl: '/static/home.html'
        };
    });


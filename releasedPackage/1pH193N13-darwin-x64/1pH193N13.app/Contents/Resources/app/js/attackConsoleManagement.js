var consolemanagementApp = angular.module('ConsoleManagementApp', []);

consolemanagementApp.controller("ConsoleManagementController",  ['$scope', function($scope) {

    
    $scope.activateSettingsPanel = false;
   
    $scope.enableSettingsButton = false 
    $scope.enableAnalysisButton = false; 
    $scope.enableGreetings = true
    $scope.enableAnalysis = false; 

    $scope.activatePresentationPanelCTF = false;
    $scope.activatePresentationPanel1pH193N13 = false;

    $scope.enableButton = " Start Simulation  "


    // $scope variables for handeling user input 

    $scope.flag = "hxp{1_r34LLy_L1k3_0r4cL3s__n0T_7h3_c0mp4nY}";
    $scope.password = "k0mpr35510n157k31N0rg4n"; 
    $scope.key = "KaPdRgUkXp2s5v8y"; 

    $scope.$watchGroup(['flag', 'password', 'key'], function(newValues, oldValues, scope) {
       

        enableFlag = ($scope.flag.length > 0 ) && (!$scope.flag.includes(" "))

        enablePassword = ($scope.password.length > 0 ) && (!$scope.password.includes(" "))

        enableKey = enableFlag = ($scope.key.length > 0 ) && (!$scope.key.includes(" "))

        if(enableFlag && enableKey && enablePassword){

            $scope.enableSettingsButton = true
        }
        else{

            $scope.enableSettingsButton = false 
        }

    });


    $scope.enableSettings = function() {
       
        $scope.enableGreetings = false;
        $scope.activatePresentationPanelCTF = !($scope.activatePresentationPanelCTF);

        if($scope.activatePresentationPanelCTF){

            $scope.enableButton = " Skip to Analysis ";
        }
        else{

            $scope.enableButton = " Start Presentation ";
            $scope.enableAnalysisPresentation()
        }
    };


    $scope.enable1pH193Ni3Presentation = function(){

        $scope.activatePresentationPanelCTF = false; 
        $scope.activatePresentationPanel1pH193N13 = true;   
        
        $scope.enableAnalysisButton = true; 
    };

    $scope.enableAnalysisPresentation = function(){

        
        $scope.enableAnalysisButton = false;
        $scope.activatePresentationPanel1pH193N13 = false;   
        $scope.activateSettingsPanel = true; 
    };


    $scope.submitSettingsData = function(){

        $scope.enableAnalysis = true; 

        crack($scope.key ,$scope.flag , $scope.password )
    };


}]);
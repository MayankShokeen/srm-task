var app=angular.module('srm-task',[]);


app.controller('srm-ctr',function($scope,$http,$timeout){


$scope.orgshow=function(){

    $http({
        method:"GET",
        url:"/org_show/",
    }).then(
    function (success){
        console.log(success.data.message);
        $scope.droporg=success.data.message;
       

         $timeout(function(){
            $scope.succ=false;
        },10000);
    },function(error){
        console.log(error.data['message']);
        $scope.err=true;
        $timeout(function(){
            $scope.err=false;
        },10000);
        $scope.error=error.data["error"];
        alert(error.data['message']);
    });

}



$scope.signup_ng=function(x=true){
    $('.loader').show();
     if ($scope.password != $scope.confirm_password){
            alert('Password does not match');
            x=false;
            return;
        }
        if(!x){
            return;
        }
	$http({
            method:"POST",
            url:"/save_user/",
            data:{
                'name':$scope.uname,
                'org_name':$scope.orgname,
                'email':$scope.email,
                'password':$scope.password,
          
            }
        }).then(
        function (success){
           
            console.log(success.data);
            $scope.success=success.data.message;
            window.location='/login/'
            $scope.succ=true;
            alert("User data saved");
             $timeout(function(){
                $scope.succ=false;
            },10000);
            
            $scope.success="Details user Saved";

        },function(error){
            
            console.log(error.data);
            $scope.err=true;
            // alert("not working");
            $timeout(function(){
                $scope.err=false;
            },10000);
            $scope.error=error.data;
            alert(error.data['message']);
        });

}


$scope.login_ng=function(){


	$http({

		method:"POST",
		url:'/login_check/',
		data:{
			'email':$scope.email,
			'password':$scope.password,
		}
	}).then(

			function(success){
			
			console.log(success.data);
			$scope.success=success.data.message;
			$scope.succ=true;
			alert("logged In");
			window.location='/upload_pic/'
			$timeout(function() {
				$scope.succ=false;
			}, 10000);

			},function(error){
			
			console.log(error.data);
			$scope.error=error.data.message;
			// alert("Its not working");
			$scope.err=true
			$timeout(function() {
				$scope.err=False;
			}, 10000);
			$scope.error=error.data;
			alert(error.data['message']);

			

			});

}


$scope.logout_ng=function(){


    $http({

        method:"POST",
        url:'/logout/',
        
    }).then(

            function(success){
            
            console.log(success.data);
            $scope.success=success.data.message;
            $scope.succ=true;
            alert("logged out");
            window.location='/'
            $timeout(function() {
                $scope.succ=false;
            }, 10000);

            },function(error){
            
            console.log(error.data);
            $scope.error=error.data.message;
            // alert("Its not working");
            $scope.err=true
            $timeout(function() {
                $scope.err=False;
            }, 10000);
            $scope.error=error.data;
            alert(error.data['message']);

            

            });

}










});




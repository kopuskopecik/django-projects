$(document).ready(function(){
	var a = 0;
	
	   $(".menu1").click(function(){
		   if (a == 0){
			   if ($(window).width() >=767){
				   $(".detailmenu").hide();
				   $(".content").attr("class", "col-md-12 col-sm-12 col-xs-12 content");
			   }
			   else {
				   $(".detailmenu").show();
				   $(".content").attr("class", "col-md-10 col-sm-9 col-xs-12 content");
			   }
			   
			   a = 1;
		   }
		   else {
			   if ($(window).width() <767){
				   $(".detailmenu").hide();
				   $(".content").attr("class", "col-md-12 col-sm-12 col-xs-12 content");
			   }
			   else {
				   $(".detailmenu").show();
				   $(".content").attr("class", "col-md-10 col-sm-9 col-xs-12 content");
			   }
			   
			   a = 0;
		   }
        	
    });
	
    
});
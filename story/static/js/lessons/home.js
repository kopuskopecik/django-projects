$(window).scroll(function() { 
	sessionStorage.scrollTop = $(this).scrollTop();

});

$(document).ready(function(){
   if (sessionStorage.scrollTop != "undefined"){
	   $(window).scrollTop(sessionStorage.scrollTop);
   }

	$(".favoriler").click(function(){
	$(this).attr("href", $(this).attr("href_url"));
	$(this).click();
	
		
	
	});
	

});
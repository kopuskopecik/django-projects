$(document).ready(function(){
	var dogru = $('#dogru-cevap').text()
	console.log(dogru)
	$("input[type=radio]").change(function(){
		console.log($("input[type=radio]:checked").val());
		if ($("input[type=radio]:checked").val() === dogru) {
			console.log("dogru çalışıyor");
			$('#dogruModal').modal("show");
		}
		else {
			console.log("yanlıs çalışıyor");
			$('#yanlisModal').modal("show");
		}		
	});
});


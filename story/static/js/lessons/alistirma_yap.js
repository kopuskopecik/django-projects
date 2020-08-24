$(document).ready(function(){
	var secilen_cevap = "";
	var secilen_soru = "";
	var sorularin_id_listesi = [];
	var dogru_cevap = "";
	var sorularin_eleman_sayisi ;
	var sira = 0;
	var kalan_eleman_sayisi;
	var redirect_url_adresi = "";
	var dogru_sayisi = 0;
	var bar_yuzdesi = 0;
	
	redirect_url_adresi = $("#url-p").text();
	console.log("Url adresi: " + redirect_url_adresi);
		
	
	$("button[dogru=dogru]").each(function(){
		$(this).siblings("div").children(".devam").before("<p class = 'text-center text-white mt-1'> Doğru Cevap: " + $(this).text() + "</p>");
		
	});
	
	
	$(".soru_listesi").each(function(){
		sorularin_id_listesi.push(this.id);
		
		if (sorularin_id_listesi.length === 1) {
			//$(this).show();
			
		}
		else {
			$(this).parent().addClass("d-none");
			
		}
	});
	
	sorularin_eleman_sayisi = sorularin_id_listesi.length
	
	$(".secenekler").click(function(){
		$(".secenekler").removeClass("btn-warning");
		$(this).addClass("btn-warning");
		
		$(this).siblings(".onaylama").prop("disabled", false).addClass("btn-success text-white");
		secilen_cevap = $(this).attr("dogru");
		
		
	
	});
	
	
	
	$(".onaylama").click(function(){
		
		$(this).prop("disabled", true);
		//$(this).removeClass("btn-success text-white");
		$(this).siblings().prop("disabled", true);
		
		$(this).addClass("d-none");
		$(this).siblings(".devamlar").removeClass("d-none");
		
		if (secilen_cevap === "dogru") {
			$(this).siblings(".devamlar").addClass("bg-success").removeClass("bg-danger");
			$(this).siblings(".devamlar").children("p").addClass("d-none");
			dogru_sayisi = dogru_sayisi + 1;
			bar_yuzdesi = (dogru_sayisi /sorularin_eleman_sayisi)*100;
			
			$(".progress-bar").css("width", bar_yuzdesi + "%");
			console.log("çalıştı mı");
			
		}
		else {
			$(this).siblings(".devamlar").addClass("bg-danger").removeClass("bg-success");
			sorularin_id_listesi.push(sorularin_id_listesi[sira])
		}
		sira = sira + 1;
		
		
	});
	
	$(".devam").click(function(){
		$(this).prop("disabled", true);
		$(this).parent().parent().addClass("d-none");
		$(this).parent().addClass("d-none");
		$(this).prop("disabled", false);
		$(this).parent().parent().children().prop("disabled", false);
		$("#soru" + sorularin_id_listesi[sira]).removeClass("d-none");
		$("#soru" + sorularin_id_listesi[sira]).children().removeClass("d-none");
		$("#soru" + sorularin_id_listesi[sira]).children(".devamlar").addClass("d-none");
		
		
		console.log("Soruların uzunlığı " + sorularin_id_listesi.length);
		console.log("Kaçıncı sırada olduğumuz " + sira);
		
		if (sorularin_id_listesi.length === sira) {
			
			$(".alert").removeClass("d-none");
			$("body").addClass("bg-success");
			
		}
		
		//console.log($("#soru" + sorularin_id_listesi[sira]));
		//console.log(sorularin_id_listesi[sira]);
		//console.log(sorularin_id_listesi);
		//console.log(sira);
		
	});
	
	$("#ajax-url").click(function(){
	$.ajax({                       // initialize an AJAX request
        url: redirect_url_adresi,		// set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'data': true       // add the country id to the GET parameters
        },
      
      });
	});
});

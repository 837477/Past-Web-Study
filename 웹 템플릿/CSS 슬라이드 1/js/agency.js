$(".btn").click(function() { 
    $("#menu,.page_cover,html").addClass("open"); // 메뉴 버튼을 눌렀을때 메뉴, 커버, html에 open 클래스를 추가해서 효과를 준다.
    window.location.hash = "#open";
}); 
			
$(".close").click(function() { 
    $("#menu,.page_cover,html").removeClass("open"); // open 클래스를 지워 원래대로 돌린다.
});
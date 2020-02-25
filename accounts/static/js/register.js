$(document).ready(function(){
	var startingYear = 1900;

    for (i = 0; i <= 2017 - startingYear; i++){
        $("#year").append($("<option></option>").val(startingYear + i).html(startingYear + i))
    }
	for (i = 1; i <= 30; i++){
        $("#day").append($("<option></option>").val(i).html(i))
    }
});
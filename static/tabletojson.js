function convertt(){
var myRows = [];
var $headers = $("th");
var $rows = $("tbody tr").each(function(index) {
  $cells = $(this).find("td");
  myRows[index] = {};
  $cells.each(function(cellIndex) {
    myRows[index][$($headers[cellIndex]).html()] = $(this).html();
  });
});

var myObj = {};
myObj.myrows = myRows;
var formData = JSON.stringify($("#myForm").serializeArray());

var myForm = document.getElementById("myForm");
                var formData = new FormData(myForm),
                obj = {};
                for (var entry of formData.entries()){
                    obj[entry[0]] = entry[1];
                }
                console.log(obj);
alert(JSON.stringify(myObj), obj);

}
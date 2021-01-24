$('#convert-table').click( function() {
  var table = $('#employeelist').tableToJSON();
  console.log(table);
  alert(JSON.stringify(table));  
});
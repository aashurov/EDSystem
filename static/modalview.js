var modalDiv = $("#modal-div");
$(".open-modal").on("click", function() {
$.ajax({
url: $(this).attr("data-href"),
success: function(data) {
modalDiv.html(data);
$("#myEdit").modal();
    }
  });
});
$(document).ready(function(){
    $("#id-add-cart").on("submit", function(event) {
      event.preventDefault();

        $.ajax({
        url: "add-to-cart/",
        type: 'POST',
        data: $(this).serialize(),
        dataType: "json",
        header: {'X-CSRFToken': '{% csrf_token %}'},
        success: function(data){
              if(data.name)
                    {
                    var html = '<tr id="item-${item.id}">';
                     html += '<td>'+data.name+'</td>';
                     html += '<td>'+data.quantity+'</td>';
                     html += '<td>'+data.total_price+'</td>';
                     html += '<td><button class="btn btn-danger form-control" onClick=\"deleteItem('+data.id+')\">DELETE</button></td></tr>';
                     $('#table_data').prepend(html);
                     $('#id-add-cart')[0].reset();
                     }
              },error: function(){
                alert(data.message);
              }
        });
    });
 });

function deleteItem(id) {
  var action = confirm("Are you sure you want to delete this item?");
  if (action != false) {
    $.ajax({
        url: "remove/",
        data: {
            "id": id,
        },
        dataType: "json",
        success: function (data) {
            if (data.deleted) {
	            $("table_data #item-" + id).remove();
	          }
            }
    });
  }
}
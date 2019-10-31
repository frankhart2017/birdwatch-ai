$(document).ready(function() {

    $("#scrape").click(function() {
        var bname = $("#bname").val();

        if(bname != "") {
          $("#status").html("Scraping please be patient....");

          $.ajax({
              url: "/scrape",
              method: "post",
              data: {"bname": bname},
              dataType: "json",
              success: function(result) {
                $("#status").html("");
                alert(result.status);
              }
          });
        } else {
          alert("Enter the name of bird!");
        }
    });

});

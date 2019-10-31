$(document).ready(function() {

    $("#augment").click(function() {
        var image = $("#image")[0].files[0];

        var form_data = new FormData();
        form_data.append('image', image);

        $.ajax({
          url: "/augment",
          method: "post",
          data: form_data,
          contentType: false,
          cache: false,
          processData: false,
          success: function(result) {
            $("#flipped-img").html("<img src='" + result.flipped_img + "'>");
            $("#left-translation-img").html("<img src='" + result.left_translation_img + "'>");
            $("#right-translation-img").html("<img src='" + result.right_translation_img + "'>");
            $("#up-translation-img").html("<img src='" + result.up_translation_img + "'>");
            alert(result.status);
          }
        });

    });

});

$(document).ready(function () {
    $("#message").focus(function () {
        $("#err").hide();
    });

    $("#send").submit(function (e) {
        message = $("#message").val().replace(/(^\s*)|(\s*$)/g, "");

        if (!message) {
            e.preventDefault();
            $("#err span").html("。。。");
            $("#err").show();
        }
    });
});
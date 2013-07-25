$(function() {
    $("#update-channel").click(function() {
        data = {data: $("#channel-field").val()}
        $.post("/config", data, function() {
            console.log("finish");
            window.location.href = "/config";
        });
    });
});

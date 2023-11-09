$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect: "bounceOut",
        },
    });

    // Siri
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });

    // Siri Message Animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "flipInX",
            sync: true,
        },
        out:{
            effect: "flipOutX",
            sync: true,
        },
    });

    // Mic Button ClickEvent
    $(micbtn).click(function () { 
        eel.playEosSound()
        $("#circle").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);

    });

})
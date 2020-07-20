var main = function(){

    var $plan1 = $('.subscription-plan-1');
    var $plan2 = $('.subscription-plan-2');

    $($plan1).click(function(){
        $('.subscription-plan-2').removeClass('selected');
        $(this).addClass('selected');
    })
    $($plan2).click(function(){
        $('.subscription-plan-1').removeClass('selected');
        $(this).addClass('selected');
    })
    //First box, effect button
    $('.btn').text("PICK TRIAL");
    $('.monthly').click(function(){
            $(this).addClass('selected');
            $('.yearly').removeClass('selected');
            $('.btn2').removeClass('btn.action');
            $('.btn1').text("CONTINUE WITH THIS GREAT OFFER!");
            $('.price1').text('9.99');
        });
    $('.yearly').click(function(){
            $(this).addClass('selected');
            $('.monthly').removeClass('selected');
            $('.btn1').text("START!");
            $('.price1').text('8.49');
        });
    //Second box, effect button
    $('.monthly1').click(function(){
            $(this).addClass('selected');
            $('.yearly1').removeClass('selected');
            $('.btn2').text("CONTINUE WITH THIS GREAT OFFER!");
            $('.price2').text('8.49 USD');
            $('.billing-frequency2').text("per month");
        });
    $('.yearly1').click(function(){
            $(this).addClass('selected');
            $('.monthly1').removeClass('selected');
            $('.btn2').text("START TRIAL");
            $('.price2').text('blah blah USD');
            $('.billing-frequency2').text("per month");
        });
}

$(document).ready(main);

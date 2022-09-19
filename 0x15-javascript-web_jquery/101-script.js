$(document).ready(function(){
    $("#add_item").click(function(){
        $("ul.my_list").append('<li>Item</li>');
    });
    $("#remove_item").click(function(){
        $("ul:first > li:eq(1)").remove();
    });
    $("#clear_list").click(function(){
        $("ul.my_list").empty();
    });
});

$( "*:contains('Enter Manually')" ).css( "color", "green" );
/*
=========================================
|                                       |
|       disableing special characters   |
|                                       |
=========================================
*/
$('.no_special_char').on('keypress', function (event) {
    var regex = new RegExp("^[a-zA-Z0-9]+$");
    var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
    if (!regex.test(key)) {
       event.preventDefault();
       return false;
    }
});



/*
=============================================
|                                           |
|       trucking company name - in gate     |
|                                           |
============================================
*/
$("#id_outer_company").on("change", function() {
    if (($(this).val() == 3) || ($(this).val() == 18) ) {
        // $( ".show-data" ).text( "yoooo" );
        $("#id_outer_company").css("color", "red");
        $("label[for='id_outer_company']").css("color", "red");
    } else {
        $("#id_outer_company").css("color", "#28166f");
        $("label[for='id_outer_company']").css("color", "#28166f");
    }
});


/*
=========================================
|                                       |
|       On Select gate check            |
|                                       |
=========================================
*/

$(".outer_company_gate").hide();
$("#out_gate label[for='id_outer_company']").hide();

$("#out_gate label[for='id_outer_company_manual']").hide();
$(".outer_company_manual_gate").hide();

$(".manual_truck_number_gate").hide();
$("#out_gate label[for='id_manual_truck_number']").hide();

$("#id_trucking_company").on("change", function() {

    if ($("#id_trucking_company").val() != 'trump transport') {
        $(".outer_company_gate").show();
        $("#out_gate label[for='id_outer_company']").show();

        $(".truck_number_gate").hide();
        $("#out_gate label[for='id_truck_number']").hide();

        $(".manual_truck_number_gate").show();
        $("#out_gate label[for='id_manual_truck_number']").show();

        $("#id_outer_company").on("change", function() {
            if ($("#id_outer_company").val() == 1) {
                $(".outer_company_manual_gate").show();
                $(".out-gate label[for='id_outer_company_manual']").show();
            } else {
                $(".outer_company_manual_gate").hide();
                $(".out-gate label[for='id_outer_company_manual']").hide();
            }
        });
    } else {
        $(".outer_company_gate").hide();
        $("#out_gate label[for='id_outer_company']").hide();

        $(".outer_company_manual_gate").hide();
        $("#out_gate label[for='id_outer_company_manual']").hide();

        $(".truck_number_gate").show();
        $("#out_gate label[for='id_truck_number']").show();

        $(".manual_truck_number_gate").hide();
        $("#out_gate label[for='id_manual_truck_number']").hide();
    }
});




/*
=========================================
|                                       |
|       On Select gate check            |
|                                       |
=========================================
*/


$(".gate-check .external-company").hide();
$(".gate-check .trucking_company").on("change", function() {
    if ($(this).val() != 1) {
        // $( ".show-data" ).text( "yoooo" );
        
        $(".gate-check .external-company").show();
    } else {
        $(".gate-check .external-company").hide();
    }
});


$(".external-truck-no").hide();
$(".truck_number").on("change", function() {
    if ($(this).val() != 1) {
        // $( ".show-data" ).text( "yoooo" );
        $(".external-truck-no").show();
    } else {
        $(".external-truck-no").hide();
    }
});



/*
=========================================
|                                       |
|       On Select in gate            |
|                                       |
=========================================
*/

$(".in-external-company").hide();
$("label[for='id_outer_company']").hide();

$("label[for='id_outer_company_manual']").hide();
$(".in-container_company_manual").hide();

$(".in-manual_truck_number").hide();
$("label[for='id_manual_truck_number']").hide();

$("#id_trucking_company").on("change", function() {

    if ($("#id_trucking_company").val() != 'trump transport') {
        $(".in-external-company").show();
        $("label[for='id_outer_company']").show();

        $(".in-truck_number").hide();
        $("label[for='id_truck_number']").hide();

        $(".in-manual_truck_number").show();
        $("label[for='id_manual_truck_number']").show();

        $("#id_outer_company").on("change", function() {
            if ($("#id_outer_company").val() == 1) {
                $(".in-container_company_manual").show();
                $("label[for='id_outer_company_manual']").show();


            } else {
                $(".in-container_company_manual").hide();
                $("label[for='id_outer_company_manual']").hide();

            }
        });
        
    } else {
        $(".in-external-company").hide();
        $(".in-truck_number").show();
        $("label[for='id_truck_number']").show();

        $(".in-manual_truck_number").hide();
        $("label[for='id_manual_truck_number']").hide();

        $(".in-container_company_manual").hide();
        $("label[for='id_outer_company_manual']").hide();
    }
});






$("#plug").hide();
$("label[for='plug']").hide();
$("#id_containerType").on("change", function() {
    if (($(this).val() == 7) || ($(this).val() == 8) ) {
        // $( ".show-data" ).text( "yoooo" );
        $("#plug").show();
        $("label[for='plug']").show();
    } else {
        $("#plug").hide();
        $("label[for='plug']").hide();
    }
});




$(".seal_number").hide();
$("label[for='id_seal_number']").hide();
$(".weight").hide();
$("label[for='id_weight']").hide();
$(".weight_type").hide();
$("label[for='id_weight_type']").hide();
$("#id_container_status").on("change", function() {
    if ($(this).val() == "load") {
        $(".seal_number").show();
        $("label[for='id_seal_number']").show();
        $(".weight").show();
        $("label[for='id_weight']").show();
        $(".weight_type").show();
        $("label[for='id_weight_type']").show();
    } else {
        $(".seal_number").hide();
        $("label[for='id_seal_number']").hide();
        $(".weight").hide();
        $("label[for='id_weight']").hide();
        $(".weight_type").hide();
        $("label[for='id_weight_type']").hide();
    }
});




/*
=========================================
|                                       |
|       On Select gate out              |
|                                       |
=========================================
*/

$(".outer_company").hide();
$("label[for='id_outer_company']").hide();

$("label[for='id_outer_company_manual']").hide();
$(".outer_company_manual").hide();

$(".manual_truck_number").hide();
$("label[for='id_manual_truck_number']").hide();

$("#id_trucking_company").on("change", function() {

    if ($("#id_trucking_company").val() != 'trump transport') {
        $(".outer_company").show();
        $("label[for='id_outer_company']").show();

        $(".truck_number").hide();
        $("label[for='id_truck_number']").hide();

        $(".manual_truck_number").show();
        $("label[for='id_manual_truck_number']").show();

        $("#id_outer_company").on("change", function() {
            if ($("#id_outer_company").val() == 1) {
                $(".outer_company_manual").show();
                $("label[for='id_outer_company_manual']").show();


            } else {
                $(".outer_company_manual").hide();
                $("label[for='id_outer_company_manual']").hide();



            }
        });
        
    } else {
        $(".outer_company").hide();
        $("label[for='id_outer_company']").hide();

        $(".outer_company_manual").hide();
        $("label[for='id_outer_company_manual']").hide();

        $(".truck_number_out").show();
        $("label[for='id_truck_number']").show();

        $(".manual_truck_number").hide();
        $("label[for='id_manual_truck_number']").hide();
    }
});


/*
=========================================
|                                       |
|           Scroll To Top               |
|                                       |
=========================================
*/ 
$('.scrollTop').click(function() {
    $("html, body").animate({scrollTop: 0});
});


$('.navbar .dropdown.notification-dropdown > .dropdown-menu, .navbar .dropdown.message-dropdown > .dropdown-menu ').click(function(e) {
    e.stopPropagation();
});

/*
=========================================
|                                       |
|       Multi-Check checkbox            |
|                                       |
=========================================
*/

function checkall(clickchk, relChkbox) {

    var checker = $('#' + clickchk);
    var multichk = $('.' + relChkbox);


    checker.click(function () {
        multichk.prop('checked', $(this).prop('checked'));
    });    
}


/*
=========================================
|                                       |
|           MultiCheck                  |
|                                       |
=========================================
*/

/*
    This MultiCheck Function is recommanded for datatable
*/

function multiCheck(tb_var) {
    tb_var.on("change", ".chk-parent", function() {
        var e=$(this).closest("table").find("td:first-child .child-chk"), a=$(this).is(":checked");
        $(e).each(function() {
            a?($(this).prop("checked", !0), $(this).closest("tr").addClass("active")): ($(this).prop("checked", !1), $(this).closest("tr").removeClass("active"))
        })
    }),
    tb_var.on("change", "tbody tr .new-control", function() {
        $(this).parents("tr").toggleClass("active")
    })
}

/*
=========================================
|                                       |
|           MultiCheck                  |
|                                       |
=========================================
*/

function checkall(clickchk, relChkbox) {

    var checker = $('#' + clickchk);
    var multichk = $('.' + relChkbox);


    checker.click(function () {
        multichk.prop('checked', $(this).prop('checked'));
    });    
}

/*
=========================================
|                                       |
|               Tooltips                |
|                                       |
=========================================
*/

$('.bs-tooltip').tooltip();

/*
=========================================
|                                       |
|               Popovers                |
|                                       |
=========================================
*/

$('.bs-popover').popover();


/*
================================================
|                                              |
|               Rounded Tooltip                |
|                                              |
================================================
*/

$('.t-dot').tooltip({
    template: '<div class="tooltip status rounded-tooltip" role="tooltip"><div class="arrow"></div><div class="tooltip-inner"></div></div>'
})


/*
================================================
|            IE VERSION Dector                 |
================================================
*/

function GetIEVersion() {
  var sAgent = window.navigator.userAgent;
  var Idx = sAgent.indexOf("MSIE");

  // If IE, return version number.
  if (Idx > 0) 
    return parseInt(sAgent.substring(Idx+ 5, sAgent.indexOf(".", Idx)));

  // If IE 11 then look for Updated user agent string.
  else if (!!navigator.userAgent.match(/Trident\/7\./)) 
    return 11;

  else
    return 0; //It is not IE
}
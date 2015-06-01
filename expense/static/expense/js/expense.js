(function($){
    jQuery = $.noConflict(true);

    function showReport(options) {
	
    }
    
    $(document).ready(function() {
	$(".reportlink").click(function (e) {
	    var x = $(this).attr('id').split("-");
	    var options = 
		{
		    chart: x[0],
		    type: x[1],
		    user: x[2]=='None'?0:x[2],
		    year: x[3]=='None'?0:x[3],
		    month: x[4]=='None'?0:x[4]
		};
	    var title = $(this).text()
	    title += x[3]=='None'?'': x[3] + '. ';
	    title += x[4]=='None'?'':x[4]+'.';

            var d = $('#dialog').html('<iframe id="ifrm" width="650" frameborder="0" height="330"></iframe>');
            d.dialog({ 
		modal: true, 
		resizable: false, 
		width: 680, 
		title: title 
	    });

	    var src = '../' + options.chart + '/' + options.user + '/' + options.type + '/' + options.year + '/' + options.month;

	    $("#dialog>#ifrm").attr("src", src);
	});
    });

})(django.jQuery);





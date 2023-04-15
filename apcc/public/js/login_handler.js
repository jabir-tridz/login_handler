$(document).ready(function(){
    if (window.location.pathname === '/app'){
        var user = frappe.session.user
        frappe.call({
            method: 'apcc.login_redirect.activity_log',
            args: {
                user: user
            },
            callback: function(r) {
                if(r.message == true){
                    window.location.href = '/success';
                }
            }
        });
    }
});
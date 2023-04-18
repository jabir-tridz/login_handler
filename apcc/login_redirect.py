import frappe

@frappe.whitelist()
def activity_log(user):
    redirect_status = False
    user_data = frappe.get_doc("User",user)
    roles = user_data.roles
    for role in roles:
        if role.role == 'System Manager':
            activity_logs = frappe.db.get_all("Activity Log",fields = ['name'], filters= {'user': user, 'operation': 'Login','status': 'Success'})
            if len(activity_logs) == 1:
                redirect_status = True
            else:
                redirect_status = False
        if role.role == 'Agent':
            redirect_status = True
    return redirect_status
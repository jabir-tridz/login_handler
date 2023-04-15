import frappe

@frappe.whitelist()
def activity_log(user):
    doctype_data = frappe.db.get_all("Activity Log",fields = ['name'], filters= {'user': user, 'operation': 'Login','status': 'Success'})
    if len(doctype_data == 1):
        return True
    else:
        return False
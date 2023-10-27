// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt

frappe.ui.form.on('GL Entry', {
	// refresh: function(frm) {

	// }
	posting_date: function(frm){
		frm.call(
			{
				doc: frm.doc,
				method: 'check_date',
				always: function (response) {
					if(response.message != undefined){
						frappe.throw(response.message)
					}
				},
			}
		)
	},
	due_date: function(frm){
		frm.call(
			{
				doc: frm.doc,
				method: 'check_date',
				always: function (response) {
					if(response.message != undefined){
						frappe.throw(response.message)
					}
				},
			}
		)
	},
});

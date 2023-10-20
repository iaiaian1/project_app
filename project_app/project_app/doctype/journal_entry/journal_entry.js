// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Journal Entry', {
	onload: function(frm){
		// Some unnecessary codes but may be useful
		// field, child_table
		frm.set_query("account", "accounting_entries", function (doc, cdt, cdn) {
			let child = locals[cdt][cdn];
				return {
				"filters": {
					docstatus: 1
				},
			};
		});
	}
});
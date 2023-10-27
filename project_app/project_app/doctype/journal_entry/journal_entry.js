// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Journal Entry', {
	refresh: function(frm) {
		if (frm.is_new()){
			// Intro
			frm.set_intro('Create a new Journal Entry', 'blue')
		}
	},
	// onload: function(frm){
	// 	frm.set_query("account", "accounting_entries", function (doc, cdt, cdn) {
	// 		let child = locals[cdt][cdn];
	// 			return {
	// 			"filters": {
	// 				docstatus: 1
	// 			},
	// 		};
	// 	});
	// },
	before_save: function(frm){
		if(frm.doc.difference != 0){
			frappe.throw("Difference is not balanced")
		}
	},
});

frappe.ui.form.on('Accounting Entries', {	
	debit: function(frm, cdt, cdn){
		let debit = 0
		let credit = 0
		frm.doc.accounting_entries.forEach(element => {
			if(element.debit || element.credit){
				debit += element.debit
				credit += element.credit
			}
		});
		frm.set_value('total_debit', debit)
		frm.set_value('total_credit', credit)
		frm.set_value('difference', Math.abs(credit - debit))
		frm.refresh()
	},

	credit: function(frm, cdt, cdn){
		let debit = 0
		let credit = 0
		frm.doc.accounting_entries.forEach(element => {
			if(element.debit || element.credit){
				debit += element.debit
				credit += element.credit
			}
		});
		frm.set_value('total_debit', debit)
		frm.set_value('total_credit', credit)
		frm.set_value('difference', Math.abs(credit - debit))
		frm.refresh()
	},

	accounting_entries_remove: function(frm){
		let debit = 0
		let credit = 0
		frm.doc.accounting_entries.forEach(element => {
			if(element.debit || element.credit){
				debit += element.debit
				credit += element.credit
			}
		});
		frm.set_value('total_debit', debit)
		frm.set_value('total_credit', credit)
		frm.set_value('difference', Math.abs(credit - debit))
		frm.refresh()
	},
});
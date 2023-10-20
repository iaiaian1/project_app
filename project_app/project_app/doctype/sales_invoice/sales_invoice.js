// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Invoice', {
	refresh: function(frm) {
		if (frm.is_new()){
			// Intro
			frm.set_intro('Create a new sales invoice', 'blue')
		}
		
		// Create payment entry button available only when form is submitted.
		// if (frm.doc.docstatus === 1){
		// 	frm.add_custom_button("Create New Payment Entry", () => {
		// 		frappe.new_doc("Payment Entry", {
		// 			// fields here
		// 			// member: member can be shortened
		// 			// naming_series: cur_frm.docname
		// 		})
		// 	})
		// }
	},

	onload: function(frm){
		// Set links filter for sales invoice Link Fields onload
		frm.set_query('customer', () => {
			return {
				filters: {
					party_type: 'customer',
					docstatus: 1
				}
			}
		})

		frm.set_query('debit_to', () => {
			return {
				filters: {
					account_type: 'Asset',
					docstatus: 1
				}
			}
		})
		frm.set_query('income_account', () => {
			return {
				filters: {
					account_type: 'Income',
					docstatus: 1
				}
			}
		})

		frm.set_value("posting_date", frappe.datetime.nowdate())
	},

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
	payment_due_date: function(frm){
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

	// items_table_on_form_rendered: function(frm){
	// 	frm.set_value()
	// },
	// on_submit: function(frm){
		
	// }
});

// Codeblock for asynchronous calculation on qty change and item table remove.
frappe.ui.form.on('Items Table', {	
	qty: function(frm, cdt, cdn){
		// This is used to access the current document table and current document name.
		let child = locals[cdt][cdn];
		child.amount = child.qty * child.rate;
		// child.amount = frm.doc.items_table[0].qty * frm.doc.items_table[0].rate;
		let total_qty= 0
		let total_amount = 0
		frm.doc.items_table.forEach(element => {
			if(element.qty){
				total_qty += element.qty
				total_amount += element.amount
			}
		});
		frm.set_value('total_qty', total_qty)
		frm.set_value('total_amount', total_amount)
		frm.refresh()
	},

	item: function(frm, cdt, cdn){
		let child = locals[cdt][cdn];
		child.amount = child.qty * child.rate;
		// child.amount = frm.doc.items_table[0].qty * frm.doc.items_table[0].rate;
		let total_qty= 0
		let total_amount = 0
		frm.doc.items_table.forEach(element => {
			if(element.qty){
				total_qty += element.qty
				total_amount += element.amount
			}
		});
		frm.set_value('total_qty', total_qty)
		frm.set_value('total_amount', total_amount)
		frm.refresh()
	},

	items_table_remove: function(frm){
		let total_qty = 0
		let total_amount = 0
		frm.doc.items_table.forEach(element => {
			if(element.qty){
				total_qty += element.qty
				total_amount += element.amount
			}
		});
		frm.set_value('total_qty', total_qty)
		frm.set_value('total_amount', total_amount)
		frm.refresh()
	},
});
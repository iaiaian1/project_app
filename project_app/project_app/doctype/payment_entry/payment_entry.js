// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payment Entry', {
	// refresh: function(frm) {

	// }
	onload: function(frm){
		let paid_from = ""
		let paid_to = ""

		if (frm.doc.payment_type == "Receive"){
			paid_from = "Asset"
			paid_to = "Income"
		}else{
			paid_from = "Liability"
			paid_to = "Expense"
		}

		frm.set_query('account_paid_from', () => {
			return {
				filters: {
					account_type: paid_from,
					docstatus: 1
				}
			}
		})
		frm.set_query('account_paid_to', () => {
			return {
				filters: {
					account_type: paid_to,
					docstatus: 1
				}
			}
		})
	},

	payment_type: function(frm){
		let paid_from = ""
		let paid_to = ""

		if (frm.doc.payment_type == "Receive"){
			paid_from = "Asset"
			paid_to = "Income"
		}else{
			paid_from = "Liability"
			paid_to = "Expense"
		}

		// console.log(paid_from)
		// console.log(paid_to)
		// debugger

		frm.set_query('account_paid_from', () => {
			return {
				filters: {
					account_type: paid_from,
					docstatus: 1
				}
			}
		})
		frm.set_query('account_paid_to', () => {
			return {
				filters: {
					account_type: paid_to,
					docstatus: 1
				}
			}
		})

		// Clear account paid from and paid to values
		frm.set_value('account_paid_from', '')
		frm.set_value('account_paid_to', '')
	}
});

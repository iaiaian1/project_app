// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payment Entry', {
	refresh: function(frm) {
		if (frm.is_new()){
			// Intro
			frm.set_intro('Create a new Journal Entry', 'blue')
		}
	},
	onload: function(frm){
		let paid_from = "Asset"
		let paid_to = "Income"

		if (frm.doc.payment_type == "Receive"){
			paid_from = "Asset"
			paid_to = "Income"
		}else{
			paid_from = "Liability"
			paid_to = "Expense"
		}

		frm.set_query('party', () => {
			return {
				filters: {
					party_type: "Customer",
					// docstatus: 1
				}
			}
		})

		frm.set_query('account_paid_from', () => {
			return {
				filters: {
					account_type: paid_from,
					// docstatus: 1
				}
			}
		})
		frm.set_query('account_paid_to', () => {
			return {
				filters: {
					account_type: paid_to,
					// docstatus: 1
				}
			}
		})
	},

	payment_type: function(frm){
		let paid_from = ""
		let paid_to = ""
		let party = ""

		if (frm.doc.payment_type == "Receive"){
			paid_from = "Asset"
			paid_to = "Income"
			party = "customer"
			frm.set_value('party_type', 'Customer')
		}else{
			paid_from = "Liability"
			paid_to = "Expense"
			party = "supplier"
			frm.set_value('party_type', 'Supplier')
		}

		// console.log(paid_from)
		// console.log(paid_to)
		// debugger

		frm.set_query('party', () => {
			return {
				filters: {
					party_type: party,
					// docstatus: 1
				}
			}
		})

		frm.set_query('account_paid_from', () => {
			return {
				filters: {
					account_type: paid_from,
					// docstatus: 1
				}
			}
		})
		frm.set_query('account_paid_to', () => {
			return {
				filters: {
					account_type: paid_to,
					// docstatus: 1
				}
			}
		})

		// Clear account paid from and paid to values
		frm.set_value('account_paid_from', '')
		frm.set_value('account_paid_to', '')
	}
});

# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalesInvoice(Document):
	# pass

	def on_submit(self):
		self.debit_gl_entry()
		self.credit_gl_entry()
		# self.new_journal()

	def debit_gl_entry(self):
		gl = frappe.new_doc('GL Entry')
		gl.posting_date = self.posting_date
		gl.due_date = self.payment_due_date
		gl.party = self.customer
		gl.account = self.debit_to
		gl.debit_amount = self.total_amount
		gl.credit_amount = 0
		gl.voucher_type = "Sales Invoice"
		gl.voucher_number = self.name + " - Asset"

		gl.insert()

	def credit_gl_entry(self):
		gl = frappe.new_doc('GL Entry')
		gl.posting_date = self.posting_date
		gl.due_date = self.payment_due_date
		gl.party = self.customer
		gl.account = self.income_account
		gl.debit_amount = 0
		gl.credit_amount = self.total_amount
		gl.voucher_type = "Sales Invoice"
		gl.voucher_number = self.name + " - Income"

		gl.insert()

	def on_cancel(self):
		frappe.db.set_value('GL Entry', self.name + " - Asset", 'is_cancelled', 1)
		frappe.db.set_value('GL Entry', self.name + " - Income", 'is_cancelled', 1)
		# breakpoint()

	# def new_journal(self):
	# 	journal = frappe.new_doc('Journal Entry')
	# 	journal.party = self.customer
	# 	journal.posting_Date = self.posting_Date
	# 	journal.append("accounting_entries", {
	# 		"account" : self.debit_to,
	# 		"party" : self.customer,
	# 		"debit" : self.total_amount,
	# 		"credit" : 0
	# 	})

	# 	journal.insert()

	@frappe.whitelist()
	def check_date(self):
		if type(self.payment_due_date) is str and type(self.posting_date) is str:
			if self.payment_due_date < self.posting_date:
				self.payment_due_date = ""
				return "Posting date end can't be earlier than Payment Due Date."
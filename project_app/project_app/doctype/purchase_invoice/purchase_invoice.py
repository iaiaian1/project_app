# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PurchaseInvoice(Document):
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
		gl.account =self.expense_account
		gl.debit_amount = self.total_amount
		gl.credit_amount = 0
		gl.voucher_type = "Purchase Invoice"
		gl.voucher_number = self.name

		gl.insert()

	def credit_gl_entry(self):
		gl = frappe.new_doc('GL Entry')
		gl.posting_date = self.posting_date
		gl.due_date = self.payment_due_date
		gl.party = self.customer
		gl.account = self.credit_to
		gl.debit_amount = 0
		gl.credit_amount = self.total_amount
		gl.voucher_type = "Purchase Invoice"
		gl.voucher_number = self.name

		gl.insert()

	@frappe.whitelist()
	def check_date(self):
		if type(self.payment_due_date) is str and type(self.posting_date) is str:
			if self.payment_due_date < self.posting_date:
				self.payment_due_date = ""
				return "Posting date end can't be earlier than Payment Due Date."

# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PaymentEntry(Document):
	# pass
	def on_submit(self):
		self.debit_gl_entry()
		self.credit_gl_entry()
		# self.new_journal()

	def debit_gl_entry(self):
		if (self.payment_type == "Receive"):
			debit_to = self.account_paid_from
		else:
			debit_to = self.account_paid_to
		gl = frappe.new_doc('GL Entry')
		gl.posting_date = self.posting_date
		gl.party = self.party
		gl.account = debit_to
		gl.debit_amount = self.amount
		gl.credit_amount = 0
		gl.voucher_type = "Payment Entry"
		gl.voucher_number = self.name + " - Debit"

		gl.insert()

	def credit_gl_entry(self):
		if (self.payment_type == "Receive"):
			credit_to = self.account_paid_to
		else:
			credit_to = self.account_paid_from
		gl = frappe.new_doc('GL Entry')
		gl.posting_date = self.posting_date
		gl.party = self.party
		gl.account = credit_to
		gl.debit_amount = 0
		gl.credit_amount = self.amount
		gl.voucher_type = "Payment Entry"
		gl.voucher_number = self.name + " - Credit"

		gl.insert()

	def on_cancel(self):
		frappe.db.set_value('GL Entry', self.name + " - Debit", 'is_cancelled', 1)
		frappe.db.set_value('GL Entry', self.name + " - Credit", 'is_cancelled', 1)

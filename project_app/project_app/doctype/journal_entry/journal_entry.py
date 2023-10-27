# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class JournalEntry(Document):
	# pass
	def before_save(self):
		# breakpoint()
		for accounting_entry in self.accounting_entries:
			# breakpoint()
			self.journal_entry(accounting_entry)

	def journal_entry(self, accounting_entry):
		gl = frappe.new_doc('GL Entry')
		gl.posting_date = self.posting_date
		gl.party = accounting_entry.party
		gl.account = accounting_entry.account
		gl.debit_amount = accounting_entry.debit
		gl.credit_amount = accounting_entry.credit
		gl.voucher_type = "Journal Entry"
		gl.voucher_number = self.name + " - " + accounting_entry.account

		gl.insert()

	def on_cancel(self):
		for accounting_entry in self.accounting_entries:
			frappe.db.set_value('GL Entry', self.name + " - " + accounting_entry.account, 'is_cancelled', 1)
			frappe.db.set_value('GL Entry', self.name + " - " + accounting_entry.account, 'is_cancelled', 1)

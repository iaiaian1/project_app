# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GLEntry(Document):
	# pass

	@frappe.whitelist()
	def check_date(self):
		if type(self.due_date) is str and type(self.posting_date) is str:
			if self.due_date < self.posting_date:
				self.due_date = ""
				return "Posting date end can't be earlier than Payment Due Date."
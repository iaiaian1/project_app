# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	if not filters:
		filters={}

	columns = get_columns()
	data = get_filtered_data(filters)
	skip_total_rows = False

	if not data:
		frappe.msgprint("No records found")
		# In case that no data is returned, swap the columns and data to retain chart
		return data, columns
	
	# This is the REQUIRED order or return empty array []
	# https://discuss.frappe.io/t/script-report-python-file-returns-advanced-use/33489/4
	# return columns, data, message, chart, report_summary
	return columns, data, None, None, None

def get_columns():
	return [
		{
			"fieldname": "name",
			"label": "Account",
			"fieldtype": "Dynamic Link",
			'options': 'Account',
			"width": 250
		},
		{
			"fieldname": "total_debit_amount",
			"label": "Total Debit Amount",
			"fieldtype": "Currency",
			"options": "currency"
			# "add_totals_row": "true"
		},
		{
			"fieldname": "total_credit_amount",
			"label": "Total Credit Amount",
			"fieldtype": "Currency",
			"options": "currency"
			# "add_totals_row": "true"
		},
	]

def get_filtered_data(filters):
	filter = get_filters(filters)
	filtered_data= {}
	filtered_data = frappe.get_all(
		doctype='GL Entry',
		fields=["account", "debit_amount", "credit_amount", "currency"],
		filters=filter,
		# order_by='account desc'
	)

	# Process data and match them to the account
	account_data = frappe.get_all(
		doctype='Account',
		fields=["name"],
	)

	# For each account, iterate the data and if they match the account, add the debit/credit to the specific account
	for account in account_data:
		account["total_debit_amount"] = 0
		account["total_credit_amount"] = 0
		for data in filtered_data:
			account["currency"] = data["currency"]
			if account.name == data.account:
				account["total_debit_amount"] += data["debit_amount"]
				account["total_credit_amount"] += data["credit_amount"]
	
	# breakpoint()

	return account_data

def get_filters(filters):
	filter = [
		{
			"is_cancelled" : 0
		}
	]
	for key, value in filters.items():
		if filters.get(key):
			filter[key] = value

	# Return a list/array of field objects with key value pair of name : query. 
	return filter

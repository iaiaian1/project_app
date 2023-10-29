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
			"fieldname": "party",
			"label": "Party",
			"fieldtype": "Dynamic Link",
			'options': 'Party'
		},
		{
			"fieldname": "account",
			"label": "Account",
			"fieldtype": "Dynamic Link",
			'options': 'Account',
			"width": 250
		},
		{
			"fieldname": "debit_amount",
			"label": "Debit Amount",
			"fieldtype": "Currency",
			"options": "currency"
			# "add_totals_row": "true"
		},
		{
			"fieldname": "credit_amount",
			"label": "Credit Amount",
			"fieldtype": "Currency",
			"options": "currency"
			# "add_totals_row": "true"
		},
		{
			"fieldname": "posting_date",
			"label": "Posting Date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"fieldname": "due_date",
			"label": "Due Date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"fieldname": "voucher_type",
			"label": "Voucher Type",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "voucher_number",
			"label": "Voucher Number",
			"fieldtype": "Link",
			"options": "GL Entry",
			"width": 250
		},
	]

def get_filtered_data(filters):
	filter = get_filters(filters)
	filtered_data= {}
	filtered_data = frappe.get_all(
		doctype='GL Entry',
		fields=['posting_date', 'due_date', "party", "account", "debit_amount", "credit_amount", "currency", "voucher_type", "voucher_number"],
		filters=filter,
		# order_by='account desc'
	)

	# filtered_data.append
	# breakpoint()

	return filtered_data

def get_filters(filters):
	filter = [
		{
			"is_cancelled" : 0
		}
	]
	for key, value in filters.items():
		if filters.get(key):
			if key == "party" or key == "account":
				filter.append({key: ['like', f'{value}%']})
			if filters.get("posting_date"):
				filter.append({key: ['>=', f'{filters.get("posting_date")}']})
			if filters.get("due_date"):
				filter.append({key: ['<=', f'{filters.get("due_date")}']})

			# if filters.get("posting_date") and filters.get("due_date"):
			# 	filter.append({key: ['between', f'{filters.get("posting_date")}' 'and', f'{filters.get("due_date")}']})
				# conditions += '"posting_date": [">=", "{}"], "modified": ["<=", "{}"]'.format(filters.get("from_date"), filters.get("to_date"))
			# filter[key]= value

	# Return a list/array of field objects with key value pair of name : query. 
	return filter

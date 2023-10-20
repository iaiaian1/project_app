# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	if not filters:
		filters={}

	columns = get_columns()
	data = get_filtered_data(filters)

	if not data:
		frappe.msgprint("No records found")
		# In case that no data is returned, swap the columns and data to retain chart
		return data, columns
	
	# This is the REQUIRED order or return empty array []
	# https://discuss.frappe.io/t/script-report-python-file-returns-advanced-use/33489/4
	# return columns, data, message, chart, report_summary
	return columns, data

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
			'options': 'Chart of Accounts',
			"width": 300
		},
		{
			"fieldname": "credit_amount",
			"label": "Total Income",
			"fieldtype": "Currency",
			"options": "currency"
		},
		{
			"fieldname": "debit_amount",
			"label": "Total Expense",
			"fieldtype": "Currency",
			"options": "currency"
		},
		{
			"fieldname": "posting_date",
			"label": "Posting Date",
			"fieldtype": "Date",
		},
		{
			"fieldname": "due_date",
			"label": "Due Date",
			"fieldtype": "Date",
		},
	]

def get_filtered_data(filters):
	filter = get_filters(filters)
	filtered_data= []
	filtered_data = frappe.get_all(
		doctype='GL Entry',
		fields=['posting_date', 'due_date', "party", "account", "debit_amount", "credit_amount", "currency"],
		filters=filter,
		# Explanation for this in the docs is NON-EXISTENT. Had to scour the source code.
		or_filters=[
			['account', 'like', '%Income'],
			['account', 'like', '%Expense'],
		]
		# order_by='account desc'
	)

	# filtered_data.append
	# breakpoint()

	# for data in filtered_data:
	# 	if (data.get("account") == "2023-Gada Electronics-Expense"):
	# 			data["total_expense"] = data.get("credit_amount")
	# 	elif (data.get("account") == "2023-Gada Electronics-Income"):
	# 		data["total_income"] = data.get("credit_amount")

	return filtered_data

def get_filters(filters):
	filter = []
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

	# filter.append({"account": ['like', '%Income', 'or', 'account', 'like', '%Expense']})
	# filter.append({"account": ['like', '2023-Gada Electronics-Expense%']})
	# Return a list/array of field objects with key value pair of name : query. 
	return filter

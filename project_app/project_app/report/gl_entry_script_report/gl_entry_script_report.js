// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["GL Entry Script Report"] = {
	"filters": [
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
		{
			"fieldname": "party",
			"label": "Party",
			"fieldtype": "Link",
            'options': 'Party'
		},
		{
			"fieldname": "account",
			"label": "Account",
			"fieldtype": "Link",
			'options': 'Chart of Accounts'
		}
	]
};

// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Profit and Loss Statement Script Report"] = {
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
	]
};

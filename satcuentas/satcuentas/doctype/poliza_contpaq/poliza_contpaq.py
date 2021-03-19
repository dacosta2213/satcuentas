# -*- coding: utf-8 -*-
# Copyright (c) 2018, CODIGO B1NAR10 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import shutil
import os
import sys
import time
from frappe.utils.file_manager import save_url
from frappe.utils import cstr

class PolizaContpaq(Document):
	pass

@frappe.whitelist()
def crear_poliza(fecha,docname):
	"""Traerse todos los movimientos"""
	movimientos = frappe.db.sql("""select no_cuenta,debit,credit,voucher_no from `tabGL Entry` where posting_date=%s""", (fecha), as_dict=1)

	site_name = cstr(frappe.local.site)
	frappe.errprint(site_name)

	f = open(site_name + "/public/files/" + docname + ".txt", "w")

	f.write("P " + str(fecha) + " 001 " + docname + "1                                                                                                          01 1" + "\n" 	)
	f.write("N   1" + "\n")
	for d in movimientos:
		if d.debit > 0:
			f.write("M " + d.no_cuenta + "               " + d.voucher_no + " 1 " + str(d.debit) + "\n")
		else:
			f.write("M " + d.no_cuenta + "               " + d.voucher_no + " 2 " + str(d.credit) + "\n")
	f.close()

	save_url("/files/" + docname + ".txt",  docname + ".txt", "Poliza Contpaq", docname , "Home/Attachments", 0) # RG-agrego el file como attachment # save_url (file_url, filename, dt, dn, folder, is_private)
	frappe.msgprint(" POLIZA CREADA EXITOSAMENTE . " + "\n"  + "<a href='javascript:void(0)' onclick='window.location.reload()'><button> RECARGAR </button></a>")

	return movimientos

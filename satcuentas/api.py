# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.utils
import frappe.sessions
import frappe.utils.file_manager
import frappe.desk.form.run_method
from frappe.utils.response import build_response
import datetime
from datetime import date
import requests
import json
import re


@frappe.whitelist()
def borrar_cuentas():
    frappe.db.sql("""delete from tabAccount""")
    print('cuentas borradas')

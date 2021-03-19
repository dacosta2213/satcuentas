// Copyright (c) 2018, CODIGO B1NAR10 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Poliza Contpaq', {
	refresh: function(frm) {

	},
	crear_poliza: function(frm) {
		if (frm.doc.__unsaved) {
			alert("La Poliza no esta guardada.")
		} else {
			frappe.call({
				      method: "satcuentas.satcuentas.doctype.poliza_contpaq.poliza_contpaq.crear_poliza",
				      args:{
							docname: frm.doc.name,
							fecha: frm.doc.fecha
						},
						callback: function (data) {
							console.log('poliza generada');
							console.log(data);
							// cur_frm.set_value("cfdi_status", "Cancelado");
						}
			})
		}
	},
});

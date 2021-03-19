## Satcuentas

Fixtures para las cuentas del SAT.

### Requisitos
- Llamar a la compañía: Temp
- Que la abreviatura sea: ERP
- Nombrar el folder /satcuentas/fixtures_master como fixtures

### Procedimiento
- Instalar ERPNEXT
- Instalar el app bench install-app satcuentas
- Correr bench migrate y bench restart
- Validar en ERPNEXT que las cuentas hayan sido cargadas
- Renombrar fixtures a fixtures_master para que no se sobreescriban los datos en bench migrate

#### License

MIT

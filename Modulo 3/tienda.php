<?php
echo "Tienda Fiorela";
echo "SELECCIONE SU METODO DE PAGO";
$metodo = 0;
switch ($metodo) {
    case 0:
        echo "TRANSFERENCIA";
        break;
    
    case 1:
        echo "PAGO MOVIL";
        break;

    case 2:
        echo "EFECTIVO";
        break;

    case 3:
        echo "ZELLE";
        break;

    default:
        # code...
        break;
}
?>
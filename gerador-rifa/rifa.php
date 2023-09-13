
<html>
	<head>
		<style type="text/css">

			* {
				font-size: 10px;
			}

			.dir {
				text-align: center;
			}
			
			.esq {
				width: 20%;
				vertical-align: top;
			}
			
			td {
			border: 2px solid black;
				height: 100px;
				padding: 10px;			
			}

			table {
				
				/*border-spacing: 0px;*/
				border-collapse: collapse;
			}
			
			@media print {
		    		table {
					page-break-before: always;
				} /* page-break-after works, as well */
			}

		</style>
	</head>
<body>

<?php

$i = 1;


for($page_rows = 1; $i<=20; $i++, $page_rows++) {

	if ($page_rows == 1)
		echo "<table>";

	$texto_esq = "Rifa Semana Acadêmica<br />Nome: ______________<br />Contato: ______________<br />";
	$texto_dir1 = "O grupo de Robótica do IFSul Jaguarão está realizando uma rifa com o intuito de adquirir equipamentos para a programação dos nossos robôs! <br />
Prêmios: 1º prêmio: jarra elétrica; 2º prêmio: kit churrasco; 3º prêmio: torradeira elétrica <br />
Sorteio: dia 24/08, 16h, no saguão do IFSul – Campus Jaguarão<br />
Obrigado pela sua participação!<br />";
	$texto_dir2 = "Nº: " . $i . " Valor R$2,00";

	echo "<tr><td class=\"esq\">$texto_esq $texto_dir2</td><td class=\"dir\">$texto_dir1 $texto_dir2</td></tr>";

	if ($page_rows == 9) {
		echo "</table>";
		$page_rows = 0;
	}
}

?>

</html>

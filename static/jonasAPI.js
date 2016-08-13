
/* -------------------------------------------------------- */
//     JONAS' LIBRARY OF GENERAL JAVASCRIPT FUNCTIONS       //
/* -------------------------------------------------------- */
//  FOUNDED: 13.08.2016
//   AUTHOR: Jonas J. Solsvik
//    PLACE: Arsettunet, Øygarden
// COMPUTER: The mac of pros - 2015
// KEYBOARD: Corsair Vengance K65 - My love
/* ------------------------------------------------------- */


function fillTable($table, arraydata, width=3){

	// It is really difficult to write something general about 
	// how to fill a table with data. Therefore in most cases it
	// is expected of the user to customize this function.
	//
	// OBJECTIVE: To fill a 2d table with 2dArray-data.
	//             The table may have n columns and n rows. 
	// INPUT:
	// 		$table    - a jQuery object of a html <tbody></tbody>
	// 		arraydata - 2d array like [[topic1, topic2, url1],[topic1, topic3, url2]]
	//      width     - specifies how many columns is shown in the table
	
	var row;
	var rowID;
	var $row;
	var cell;

	for(var i=0; i < arraydata.length; i++){

		// Construct each row with a unique row ID.
		row = arraydata[i];
		rowID = 'rowid_'+i;
		$table.append('<tr id="' + rowID + '"></tr>');
		$row = $('#'+rowID);

		for (var j=0; j<width; j++){
			cell =  row[j];

			switch(j){
				case 0:
					$row.append('<td>'+ cell +'</td>');
					break;
				case 1:
					$row.append('<td>'+ cell +'</td>');
					break;
				case 2:
					$row.append('<td>'+ cell +'</td>');
					break;
			};
		};
	};
};


function deepCopy(oldValue) {
  // Deep copy/clone hack of a JAVASCRIPT object
  var newValue
  strValue = JSON.stringify(oldValue)
  return newValue = JSON.parse(strValue)
};


REGEX = {
	urlpattern1 : /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/,
	urlpattern2 : /^(https?|ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(\#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i
};



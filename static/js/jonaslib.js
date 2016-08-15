
/* -------------------------------------------------------- */
//     JONAS' LIBRARY OF GENERAL JAVASCRIPT PROCEDURES      //
/* -------------------------------------------------------- */
//      FIL: jonaslib.js
//  FOUNDED: 13.08.2016
//   AUTHOR: Jonas J. Solsvik
//    PLACE: Arsettunet, Øygarden
// COMPUTER: The mac of pros - 2015
// KEYBOARD: Corsair Vengance K65 - My love
/* ------------------------------------------------------- */


function revealHiddenRow($row){
	// OBJECTIVE:
	//		Reveal a row just beneath a row with a click-handler.
	//       The new row is supposed to show extra information.
	// INPUT:
	//    jQuery - row : The row number which was clicked.

	var url;
	var num;
	var $insobject;

	if (!$('#'+$row.id+'edit').length){ 
		num = $row.id.split('_')[1];

		// Extract url from row
		url = $('#urlkey_'+num).html();

		$insobject = $('<tr id="'+$row.id+'edit">'+ 
			             '<td ><input type="text" placeholder="Change maintopic"/></td>' +
			             '<td ><input type="text" placeholder="Change subtopic"/></td>"'+
			             '<td ><button>SUBMIT CHANGE</button></td>'+
			             '<td ><button>DELETE ROW</button></td>'+
			           '</tr>');

		$insobject.insertAfter($row);
	} else {
		$('#'+$row.id+'edit').remove();
	};
};


function fillTable_2d($tbody, arraydata, width=3){

	// THOUGHTS:
	// 		It is really difficult to write something general about 
	// 		how to fill a table with data. Therefore in most cases it
	// 		is expected of the user to customize this function.
	//
	// OBJECTIVE: To fill a 2d table with 2dArray-data.
	//             The table may have n columns and n rows. 
	//
	// INPUT:
	// 		jQuery - tbody     - a jQuery object of a html <tbody></tbody>
	// 		array  - arraydata - eks. [[topic1, topic2, url1],[topic1, topic3, url2]]
	//      int    - width     - specifies how many columns is shown in the table
	
	var row;
	var rowID;
	var $row;
	var cell;
	
	var maintopic;
	var subtopic;
	var url;

	console.log("TABLE lenght: " + arraydata.length);

	for(var i=0; i < arraydata.length; i++){

		// Construct each row with a unique row ID.
		row = arraydata[i];
		rowID = 'rowid_'+i;
		$tbody.append('<tr id="' + rowID + '" class="mainrow"></tr>');
		$row = $('#'+rowID);

		$row.click(function(){
			revealHiddenRow(this);
		});
		url = row[2];
		title = LINKSDATA[url].title.slice(0, 40) + '...';

		for (var j=0; j < width; j++){
			cell =  row[j];

			switch(j){
				case 0:
					$row.append('<td><td><img width="40px" height="40px" src="'+LINKSDATA[url].favicon+'"/></td></td>');
					$row.append('<td>'+ cell +'</td>');
					break;
				case 1:
					$row.append('<td>'+ cell +'</td>');
					break;
				case 2:
					$row.append('<td id="urlkey_'+i+'">'+ title +'</td>');
					$row.append('<td><a href="'+url+'"><i class="fa fa-external-link fa-4" aria-hidden="true"></i></a></td>');
					// <i class="fa fa-times fa-4" aria-hidden="true"></i>
					break;
			};
		};
	};
};


function generalSearch (array, sentence, limitTo=-10000, onerow=false) {
    
    //  THOUGHTS:
    //         This search method is fast enough for live search. 
    //          I have to check if it is faster to move variable declarations
    //           outside function, and other ways of making it faster.
    //  
    //	OBJECTIVE:  A function that searches any column in a 2d-array
    //                      for any word in a string-sentence.
	//	
	//  INPUT:
	//		 array  -  array = [[something,some more, even more],[bla, bla bla]]
	//	                Array does not need to have a static number of rows and columns.
	//		 string -  sentence = "This is a sentencce 2345 +1#?=¤="
	//		 int    -  limitTo = 0,1...n - index of column limited to
	//		 bool   -  onerow =  if True - returns the first row that matches
    
    var trimmedArray = [];
    var kwords = '';
	var kwordsLength = 0;
	var wordsCorrect = 0;
	var row = '';

    kwords = sentence.split(' ');
	kwordsLength = kwords.length;

    /*Loop through rows, and make the rows toString() for faster searching.*/
    for (i=0; i<array.length; i++){

    	if (limitTo >= 0){
    		/* Limit columns that are searched*/
    		row = array[i][limitTo].toString().toUpperCase();
    	} else {
        	row = array[i].toString().toUpperCase();
    	};

        for (j=0; j < kwordsLength; j++){
            if (row.indexOf(kwords[j].toUpperCase()) > -1){
                wordsCorrect += 1;
            };
        };
        /*console.log("Correct: " + wordsCorrect + '| kwordsLength: ' + kwordsLength)*/

        if (onerow){
        	if (wordsCorrect == kwordsLength){
            	trimmedArray.push(array[i]);
                wordsCorrect = 0;   
            	return trimmedArray;
        	};
        } else {
        	if (wordsCorrect == kwordsLength){
            	trimmedArray.push(array[i]);
        	};
        };
        wordsCorrect = 0;
    };
    return trimmedArray;
};


function deepCopy(base) {
  // OBJECTIVE:
  // 	Create a  deep copy of a Javascript object.
  // INPUT:
  // 	JSON-object - base - could be any object in Javascript
  // RETURN:
  //    JSON-object - copy - returns the new deep copy 

  var copy;
  var strValue;

  strValue = JSON.stringify(base);
  copy = JSON.parse(strValue);

  return copy;
};


REGEX = {
	urlpattern1 : /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/,
	urlpattern2 : /^(https?|ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(\#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i
};



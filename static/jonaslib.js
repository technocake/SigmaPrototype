
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
	console.log(arraydata.length);
	
	for(var i=0; i < arraydata.length; i++){

		// Construct each row with a unique row ID.
		row = arraydata[i];
		rowID = 'rowid_'+i;
		$tbody.append('<tr id="' + rowID + '"></tr>');
		$row = $('#'+rowID);

		for (var j=0; j < width; j++){
			cell =  row[j];

			switch(j){
				case 0:
					$row.append('<td><td><img width="40px" height="40px" src="#"/></td></td>');
					$row.append('<td>'+ cell +'</td>');
					break;
				case 1:
					$row.append('<td>'+ cell +'</td>');
					break;
				case 2:
					$row.append('<td>'+ cell +'</td>');
					$row.append('<td><a id="#" class="linkholder" href="#"><img width="25px" height="25px" src="static/external_link.png"/></a></td>');
					break;
			};
		};
	};
};



function generalSearch (array, sentence, limitTo=-10000, onerow=false) {
    
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



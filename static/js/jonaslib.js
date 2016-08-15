
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



/*
	sigma.js

	For speaking with a sigma engine.	
*/

var sigma = {
	/*
	 *	#########################	fetchlinks	#############################
	 *  #
	 *	#	doc: https://github.com/technocake/SigmaPrototype/blob/master/DOCS/sigma-api/fetchlinks.md
	 *	#
	 */
	fetchlinks: function(handler) {
		$.get('/fetchlinks', function(data){
			handler(data);
		});
	},


	/*
	 *	#########################	fetchsearchdata	#############################
	 *  #
	 *	#	doc: https://github.com/technocake/SigmaPrototype/blob/master/DOCS/sigma-api/fetchsearchdata.md
	 *	#
	 */
	fetchsearchdata: function(handler) {
		$.post('/fetchsearchdata', function(data){
			handler(data);
		});
	},


/*
	 *	#########################	mapnames	#############################
	 *  #
	 *	#	doc: https://github.com/technocake/SigmaPrototype/blob/master/DOCS/sigma-api/mapnames.md
	 *	#
	 */
	mapnames: function(handler, error_handler) {
		$.get('/mapnames', function(data){
        	if (data.status === 'Names OK'){
				handler(data);
			}
			else {
				if (error_handler === undefined) {
					console.log(data.status);
				}
				else {
					error_handler(data);
				}
			}
		});
	},



	/*
	 *	#########################	tags	#############################
	 *  #
	 *	#	doc: https://github.com/technocake/SigmaPrototype/blob/master/DOCS/sigma-api/tags.md
	 *	#
	 */
	tags: function(handler) {
		$.get('/tags', function(data){
			handler(data);
		});
	},


	/*
	 *	#########################	users	#############################
	 *  #
	 *	#	doc: https://github.com/technocake/SigmaPrototype/blob/master/DOCS/sigma-api/fetchlinks.md
	 *	#
	 */
	users: function(handler) {
		$.get('/users', function(data){
			handler(data);
		});
	},



	/*
	 *	#########################	getmap	#############################
	 *  #
	 *	#	doc: https://github.com/technocake/SigmaPrototype/blob/master/DOCS/sigma-api/getmap.md
	 *	#
	 */
	getmap: function(mapid, handler, error_handler) {
		$.ajax('/getmap', {
            data : JSON.stringify({ 'mapid' : mapid }),
            contentType : 'application/json',
            type : 'POST',
            success : function(data){
	                handler(data);
                },
            error : function(data)
            	{
	              if (error_handler === undefined) {console.log(data.status);}
				  else { error_handler(data); }
                }
            });
	},



	/* -----------------	Updating calls  --------------------- */

	postmeta: function(meta, handler, error_handler) {
		$.ajax('/postmeta', {
            data : JSON.stringify(meta),
            contentType : 'application/json',
            type : 'POST',
            success : function(data){
            		console.log(data.status);
	                handler(data);
                },
            error : function(data)
            	{
	              if (error_handler === undefined) {console.log(data.status);}
				  else { error_handler(data); }
                }
            });
	},


	updatemap: function(mapdata, handler, error_handler) {
		$.ajax('/updatemap', {
            data : JSON.stringify(mapdata),
            contentType : 'application/json',
            type : 'POST',
            success : function(data){
            		console.log(data.status);
	                handler(data);
                },
            error : function(data)
            	{
	              if (error_handler === undefined) {console.log(data.status);}
				  else { error_handler(data); }
                }
            });
	}


}
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
	}
}
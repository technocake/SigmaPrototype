/* CONFIG.js */


CONF = {

    // Rules - mapssvg.html

    // DISCUSSION:
    // I have grouped similar properties together so far, 
    // but it might make more sense, to group objects together going forward.
    // I am undecided.


    // These two pairs, determines how far away from their mothernode the childnodes should appear.
    // We use relative coordinates here, so 100/100 would be 100% of the screen width.

    subradx: 27/100,
    subrady: 25/100,
    urlradx: 9/100,
    urlrady: 5/100,

    // Here we determine the size of the node bodies... 
    // The number represents the raidus of the circle in pixels.
    main_size: 15,
    sub_size: 9,
    url_size: 5,

    // ..and the size of their text
    // CSS font-size in px.
    main_size_text: '22px',
    sub_size_text: '18px',
    url_size_text: '15px',

    // COLORS
    // Node body colors
    //main_color: 'stroke: #00e673; fill: #00e673;',
    main_color: 'stroke: #4e4e4e; fill: #4e4e4e;',
    sub_color: 'stroke: #4e4e4e; fill: #4e4e4e;',
    url_color: 'stroke: #4e4e4e; fill: #4e4e4e;',
   
    // pure data
    sub_fillcolor: '#4e4e4e',
    url_fillcolor: 'red',
    main_fillcolor: 'red',

    //hilighting
    hilight_color: 'yellow',

    // Line color
    line_color: 'stroke: #808080; stroke-width: 1.5px;',

    // Node text colors
    main_color_text: 'black',
    sub_color_text:  'black',
    url_color_text:  'black',



    bottom_of_config: 'Bye bye! :)'
}
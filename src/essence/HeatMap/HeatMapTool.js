//New Tool Template
import $ from 'jquery'
import F_ from '../../Basics/Formulae_/Formulae_'
import L_ from '../../Basics/Layers_/Layers_'
import Map_ from '../../Basics/Map_/Map_'
import * as d3 from 'd3'
//Add the tool markup if you want to do it this way

// prettier-ignore
const markup = [
    `<div id='newTool'>`,
    `</div>`
].join('\n');

const NewToolTemplate = {
    height: 0,
    width: 300,
    MMGISInterface: null,
    make: function () {
        this.MMGISInterface = new interfaceWithMMGIS()
    },
    destroy: function () {
        //this.MMGISInterface.separateFromMMGIS()
    },
    getUrlString: function () {
        // Return the path to the generated heatmap HTML file
        return '\Users\User\Documents\GitHub\MMGIS\src\essence\Tools\HeatMap\spatial_heatmap.html'; // Replace with the actual path //HELLOOOOOOOOOOOOOOOOOOOOOOOOOO
    },
    
}

//
function interfaceWithMMGIS() {



    //MMGIS should always have a div with id 'toolPanel'
    let tools = d3.select('#toolPanel')
    tools.style('background', 'var(--color-k)')
    //Clear it
    tools.selectAll('*').remove()

    //ytools = tools.append('div').style('height', '100%')
     // Add an iframe to display the heatmap HTML file
     const iframe = document.createElement('iframe');
     iframe.src = NewToolTemplate.getUrlString(); // Use the getUrlString method to get the URL
     iframe.style.width = '100%';
     iframe.style.height = '100%';
 
     // Append the iframe to the tool's div
     tools.node().appendChild(iframe);
    
}

//Other functions

export default NewToolTemplate

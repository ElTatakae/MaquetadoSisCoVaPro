document.addEventListener('DOMContentLoaded', function() {
var myConfig = {
 	type: "line",
 	title:{
 	  text:"Indicadores de control",
 	},
 	subtitle:{
 	  text:""
 	},
 	scaleY:{
 	  markers:[
 	    {
 	      type:"line",
 	      range:[85],
 	      lineColor:"red",
 	      lineWidth: 5,
 	      lineStyle: "dotted",
 	      label:{
 	        text:"Critical",
 	        backgroundColor:"red",
 	        fontColor:"white",
 	        fontSize: 14,
 	      }
 	    },
 	    {
 	      type:"line",
 	      range:[60],
 	      lineColor:"blue"
 	    },
 	    {
 	      type:"line",
 	      range:[41],
 	      lineColor:"cyan",
 	      lineWidth: 2
 	    },
 	    {
 	      type:"line",
 	      range:[17],
 	      lineStyle: "dashed",
 	      lineWidth: 2,
 	      lineColor:"orange",
 	      labelPlacement: "opposite",
 	      label:{
 	        text:"Limite inferior/<br>"
 	      }
 	    }
    ],
 	},
	series : [
		{
			values : [34, 93, 46, 100, 33, 78, 10, 24, 92, 77, 12, 1],
			lineColor:"#333",
			marker:{
			  backgroundColor:"#333"
			}
		},
		{
			values : [8, 46, 65, 79, 93, 77, 31, 24, 90, 53, 9, 81],
			lineColor:"#787878",
			marker:{
			  backgroundColor:"#787878"
			}
		},
		{
			values : [23, 93, 34, 72, 96, 33, 32, 27, 38, 49, 75, 74],
			lineColor:"#a1a1a1",
			marker:{
			  backgroundColor:"#a1a1a1"
			}
		}
	]
};

zingchart.render({
	id : 'myChart',
	data : myConfig,
	height: 400,
	width: '100%'
});
});
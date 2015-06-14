var diameter = 960;
var currentId = 0;

// trading graph
var tradingGraph = function(){
	var margin = {top: 30, right: 20, bottom: 30, left: 20},
		widthMinusMargin = diameter - margin.left - margin.right,
		barHeight = 20,
		barWidth = widthMinusMargin * .8;

	var i = 0,
		duration = 400,
		root;

	var tree = d3.layout.tree()
		.nodeSize([0, 20]);

	var diagonal = d3.svg.diagonal()
		.projection(function(d) { return [d.y, d.x]; });

	var svg = d3.select(".trading-graph").append("svg")
		.attr("width", diameter)
		.attr('viewBox', '0 0 ' + diameter + ' ' + diameter)
		.attr('preserveAspectRatio', 'xMinYMin meet')
		.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	d3.json("data.json", function(error, rowData) {

		var data = rowData.data[currentId];
		var rootNode = {
			"name": data.company,
			"children": data.trading
		};

		$("#company-name-main").text(rootNode.name);

		if (error) throw error;

		rootNode.x0 = 0;
		rootNode.y0 = 0;
		update(root = rootNode);
	});

	function update(source) {

		// Compute the flattened node list. TODO use d3.layout.hierarchy.
		var nodes = tree.nodes(root);

		var height = Math.max(500, nodes.length * barHeight + margin.top + margin.bottom);

		d3.select("svg").transition()
			.duration(duration)
			.attr("height", height);

		d3.select(self.frameElement).transition()
			.duration(duration)
			.style("height", height + "px");

		// Compute the "layout".
		nodes.forEach(function(n, i) {
			n.x = i * barHeight;
		});

		// Update the nodes…
		var node = svg.selectAll("g.node")
			.data(nodes, function(d) { return d.id || (d.id = ++i); });

		var nodeEnter = node.enter().append("g")
			.attr("class", "node")
			.attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
			.style("opacity", 1e-6);

		// Enter any new nodes at the parent's previous position.
		nodeEnter.append("rect")
			.attr("y", -barHeight / 2)
			.attr("height", barHeight)
			.attr("width", barLen)
			.style("fill", color);

		nodeEnter.append("text")
			.attr("dy", 3.5)
			.attr("dx", 5.5)
			.text(function(d) { return d.name; });

		// Transition nodes to their new position.
		nodeEnter.transition()
			.duration(duration)
			.attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; })
			.style("opacity", 1);

		node.transition()
			.duration(duration)
			.attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; })
			.style("opacity", 1)
			.select("rect")
			.style("fill", color);

		// Transition exiting nodes to the parent's new position.
		node.exit().transition()
			.duration(duration)
			.attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
			.style("opacity", 1e-6)
			.remove();

		// Update the links…
		var link = svg.selectAll("path.link")
			.data(tree.links(nodes), function(d) { return d.target.id; });

		// Enter any new links at the parent's previous position.
		link.enter().insert("path", "g")
			.attr("class", "link")
			.attr("d", function(d) {
				var o = {x: source.x0, y: source.y0};
				return diagonal({source: o, target: o});
			})
			.transition()
			.duration(duration)
			.attr("d", diagonal);

		// Transition links to their new position.
		link.transition()
			.duration(duration)
			.attr("d", diagonal);

		// Transition exiting nodes to the parent's new position.
		link.exit().transition()
			.duration(duration)
			.attr("d", function(d) {
				var o = {x: source.x, y: source.y};
				return diagonal({source: o, target: o});
			})
			.remove();

		// Stash the old positions for transition.
		nodes.forEach(function(d) {
			d.x0 = d.x;
			d.y0 = d.y;
		});
	}

	function color(d) {
		return d._children ? "#3182bd" : d.children ? "#c6dbef" : "#fd8d3c";
	}

	function barLen(d) {
		return d.children ? barWidth : barWidth * d.size;
	}
};
tradingGraph();


var keywordGraph = function() {
		var format = d3.format(",d"),
		color = d3.scale.category20c();

	var bubble = d3.layout.pack()
		.sort(null)
		.size([diameter, diameter])
		.padding(1.5);

	var svg = d3.select(".keywords-graph").append("svg")
		.attr("width", diameter)
		.attr("height", diameter)
		.attr('viewBox', '0 0 ' + diameter + ' ' + diameter)
		.attr('preserveAspectRatio', 'xMinYMin meet')
		.attr("class", "bubble");

	d3.json("data.json", function(error, root) {
		if (error) throw error;


		var data = root.data[currentId];
		var rootNode = {
			"name": data.company,
			"children": data.keywords
		};

		var node = svg.selectAll(".node")
			.data(bubble.nodes(classes(rootNode))
				.filter(function(d) { return !d.children; }))
			.enter().append("g")
			.attr("class", "node")
			.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

		node.append("title")
			.text(function(d) { return d.className + ": " + format(d.value); });

		node.append("circle")
			.attr("r", function(d) { return d.r; })
			.style("fill", function(d) { return color(d.packageName); });

		node.append("text")
			.attr("dy", ".3em")
			.style("text-anchor", "middle")
			.text(function(d) { return d.className.substring(0, d.r / 3); });
	});

// Returns a flattened hierarchy containing all leaf nodes under the root.
	function classes(root) {
		var classes = [];

		function recurse(name, node) {
			if (node.children) node.children.forEach(function(child) { recurse(node.name, child); });
			else classes.push({packageName: name, className: node.name, value: node.size});
		}

		recurse(null, root);
		return {children: classes};
	}

	d3.select(self.frameElement).style("height", diameter + "px");
};
keywordGraph();

$( ".retry" ).click(function() {
	currentId = currentId == 0 ? 1 : 0;
	d3.select(".trading-graph").selectAll("svg").remove();
	d3.select(".keywords-graph").selectAll("svg").remove();
	tradingGraph();
	keywordGraph();
});
package org.opentripplanner.model.json_serialization;

import org.opentripplanner.routing.graph.Graph;

public class WithGraph {
    private /*@ spec_public @*/  Graph graph;
    private /*@ spec_public @*/ Object object;
    public WithGraph(Graph graph, Object object) {
        this.graph = graph;
        this.object = object;
    }
    //@ requires graph != null;
    public Graph getGraph() {
        return graph;
    }
    
    //@ requires object != null;
    public Object getObject() {
        return object;
    }
    
}

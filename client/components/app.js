import React from "react";
import Card from "./Card";
import Search from "./Search";


export default class App extends React.Component{
    render(){
        return(
            <React.Fragment>
                <Search></Search>
                <div className="row">
                    <Card classN="col-md-4"></Card>
                    <Card classN="col-md-4"></Card>
                    <Card classN="col-md-4"></Card>
                </div>
            </React.Fragment>
        );
    }
}
import React from "react";

import axios from 'axios';

import Card from "./Card";
import Search from "./Search";


export default class App extends React.Component{
    constructor(props){
        super(props);
        this.props = props;
        this.state = {  };
    }
    componentDidMount(){
        axios.get('http://127.0.0.1:8000/game/')
            .then((result) => {
                let data = result.data.results;
                this.setState({
                    data
                })
            })
    }
    render(){
        let { data } = this.state;
        return(
            <React.Fragment>
                <Search></Search>
                {
                    data ? data.map((value, index) => {
                        return (
                            <Card value={value} classN="col-md-12"></Card>
                        );
                    }) : ''
                }
                {/* <div className="row">
                    <Card classN="col-md-3"></Card>
                    <Card classN="col-md-3"></Card>
                    <Card classN="col-md-3"></Card>
                    <Card classN="col-md-3"></Card>
                </div> */}
            </React.Fragment>
        );
    }
}
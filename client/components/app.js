import React from "react";

import axios from 'axios';

import Card from "./Card";
import Search from "./Search";
require('jquery-ui-bundle');


export default class App extends React.Component{
    constructor(props){
        super(props);
        this.props = props;
        this.state = {  };
        this.search = React.createRef();
        this._handle_search = this._handle_search.bind(this)
    }
    componentDidMount(){
        axios.get('api/v1/game/')
            .then((result) => {
                let data = result.data.results;
                this.setState({
                    data
                })
            })
        this.search.current.search.current.focus();
    }
    _handle_search(event){
        const search = this.search.current.search.current;
        axios.get('api/v1/search/game/', {'name': search.value})
            .then((result) => {
                let data = []
                result.data.results.map(item => data.push(item.name));
                console.log(data);
                $('#search').autocomplete({source: data});
            })
    }

    render(){
        let { data } = this.state;
        return(
            <React.Fragment>
                <Search onChange={this._handle_search} ref={this.search} />
                {
                    data ? data.map((value, index) => {
                        return (
                            <Card key={index} value={value} classN="col-md-12"></Card>
                        );
                    }) : ''
                }
                <div className="pagination">
                    <span onClick={this.nextPage}>
                        <i className={'fas fa-chevron-circle-left'}></i>
                    </span>
                    <span onClick={this.nextPage}>
                        <i className={'fas fa-chevron-circle-right'}></i>
                    </span>
                </div>
            </React.Fragment>
        );
    }
}
import React from "react";

import axios from "axios";

import "./search.scss"

export default class Search extends React.Component{
    constructor(props){
        super(props);
        this.props = props;
        this.state = {  };
        this.search = React.createRef();
    }

    render(){
        const {onChange} = this.props;
        return(
            <div className="row search">
                <div className="col-md-12">
                    <div className="input-group">
                        <input id="search" onChange={onChange} ref={this.search} className="form-control border-secondary py-2" type="search" placeholder="search..." />
                        <div className="input-group-append">
                            <button className="btn btn-outline-secondary" type="button">
                                <i className="fa fa-search"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
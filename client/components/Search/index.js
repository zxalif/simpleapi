import React from "react";

import "./search.scss"

export default class Search extends React.Component{
    constructor(props){
        super(props);
        this.props = props;
    }
    render(){
        return(
            <div className="row search">
                <div className="col-md-12">
                    <div className="input-group">
                        <input className="form-control border-secondary py-2" type="search" placeholder="search..." />
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
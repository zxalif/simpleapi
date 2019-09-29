import React from "react";

import "./card.scss"

class Card extends React.Component{
    constructor(props){
        super(props);
        this.props = props;
    }
    render(){
        const { classN, value } = this.props;
        return(
            <div className={ (classN ? classN : 'col-md-12') + ' ' + 'card' }>
                <div className="box">
                    <div className="img">
                        <img src={ value.image } />
                    </div>
                    <h2>{ value.category.name }<br /><span>{ value.name }</span></h2>
                    <p> { value.description }</p>
                    <span>
                <ul>
                    <li><a href="#"><i className="far fa-heart"  aria-hidden="true" /></a></li>
                    <li><a href="#"><i className="fas fa-comment-dots"  aria-hidden="true" /></a></li>
                    <li><a href="#"><i className="fab fa-facebook-f"  aria-hidden="true" /></a></li>
                    <li><a href="#"><i className="far fa-thumbs-down"  aria-hidden="true" /></a></li>
                    <li><a href="#"><i className="fas fa-glasses"  aria-hidden="true" /></a></li>
                </ul>
                </span>
                </div>
            </div>
        );
    }
}

export default Card;
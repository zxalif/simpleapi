import React from "react";

import "./card.scss"

class Card extends React.Component{
    constructor(props){
        super(props);
        this.props = props;
    }
    render(){
        const { classN } = this.props;
        return(
            <div className={ (classN ? classN : 'col-md-12') + ' ' + 'card' }>
                <div className="box">
                    <div className="img">
                        <img src="/media/19688321_143404322878614_1977351481_o.jpg" />
                    </div>
                    <h2>Prakash Prajapati<br /><span>Web Graphic Designer</span></h2>
                    <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et.</p>
                    <span>
                <ul>
                    <li><a href="#"><i className="fa fa-facebook" aria-hidden="true" /></a></li>
                    <li><a href="#"><i className="fa fa-twitter" aria-hidden="true" /></a></li>
                    <li><a href="#"><i className="fa fa-google-plus" aria-hidden="true" /></a></li>
                    <li><a href="#"><i className="fa fa-linkedin" aria-hidden="true" /></a></li>
                    <li><a href="#"><i className="fa fa-instagram" aria-hidden="true" /></a></li>
                </ul>
                </span>
                </div>
            </div>
        );
    }
}

export default Card;
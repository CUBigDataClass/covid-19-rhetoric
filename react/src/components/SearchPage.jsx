import React from "react";
import TopNavBar from "./TopNavBar"
import TweetCard from "./TweetCard"
import SearchForm from "./SearchForm"
import '../CSS/App.css';

export default class SearchPage extends React.Component {

    constructor(props) {
        super(props)
        this.state = { tweetIds: [] }
    }

    render() {
        return (
            <div className="App">
                <TopNavBar />
                <dl className="dictionary">{this.state.tweetIds.map(this.createTwitterCard)}</dl>
            </div>
        );
    }
}

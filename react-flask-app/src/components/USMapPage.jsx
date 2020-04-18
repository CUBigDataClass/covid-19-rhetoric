import React from "react";
import TopNavBar from "./TopNavBar"
import TweetCard from "./TweetCard"
import '../CSS/App.css';
import USAMap from "react-usa-map";


export default class USMapPage extends React.Component {


    constructor(props) {
        super(props)
        this.state = { tweetIds: [] }
    }


    mapHandler = (event) => {
        //alert(event.target.dataset.name);
        var state_name = event.target.dataset.name
        var vm = this
        fetch('/GetTopPostsState/' + state_name).then(res => res.json()).then(data => {
            vm.setState({
                tweetIds: data
            })
        })
    };


    createTwitterCard(tweetId) {
        console.log(tweetId)
        return (
            <TweetCard
                key={tweetId}
                tweetId={tweetId}
            />
        );
    }

    render() {
        return (
            <div className="App">
                <TopNavBar />
                <h1>Top Tweets in the US</h1>
                <USAMap onClick={this.mapHandler} />
                <h3>Results:</h3>
                <dl className="dictionary">{this.state.tweetIds.map(this.createTwitterCard)}</dl>
            </div>
        );
    }
}

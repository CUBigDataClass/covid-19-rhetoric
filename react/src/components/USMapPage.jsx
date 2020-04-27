import React from "react";
import TopNavBar from "./TopNavBar"
import TweetCard from "./TweetCard"
import '../CSS/App.css';
import USAMap from "react-usa-map";


export default class USMapPage extends React.Component {


    constructor(props) {
        super(props)
        this.state = { tweets: [] }
    }


    mapHandler = (event) => {
        //alert(event.target.dataset.name);
        var state_name = event.target.dataset.name
        var vm = this
        fetch('https://backend-dot-bigdata-covid.uc.r.appspot.com/GetTopPostsState/' + state_name).then(res => res.json()).then(data => {
            vm.setState({
                tweets: data
            })
        })
    };


    createTwitterCard(tweet) {
        var tweetId = tweet.key;
        var polarity = tweet.sentiment;
    
        var bg = "";
        if (polarity >= -0.5 && polarity <= 0.5) bg = "Light";
        else if (polarity > 0.5) bg = "Success";
        else bg = "Danger";
    
        return <TweetCard key={tweetId} tweetId={tweetId} bg={bg} />;
    }

    render() {
        return (
            <div className="App">
                <TopNavBar />
                <h1>Top Tweets in the US</h1>
                <USAMap onClick={this.mapHandler} />
                <h3>Results:</h3>
                <dl className="dictionary">{this.state.tweets.map(this.createTwitterCard)}</dl>
            </div>
        );
    }
}

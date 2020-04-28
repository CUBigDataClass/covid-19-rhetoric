import React from "react";
import TopNavBar from "./TopNavBar";
import TweetCard from "./TweetCard";
import "../CSS/App.css";

export default class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = { tweets: [] };
  }

  
  computeSentiment(polarity) {
    console.log("inside compute sentiment---")
  
  }
  createTwitterCard(tweet) {
    console.log("logging this...")
    var tweetId = tweet.key;
    var polarity = tweet.sentiment;

    var bg = "";
    if (polarity >= -0.5 && polarity <= 0.5) bg = "Light";
    else if (polarity > 0.5) bg = "Success";
    else bg = "Danger";

    return <TweetCard key={tweetId} tweetId={tweetId} bg={bg} />;
  }

  

  componentDidMount() {
    var vm = this;
    fetch("/GetSentimentHomePage")
      .then((res) => res.json())
      .then((data) => {
         vm.setState({
           tweets: data.slice(0,100),
         });
      });
  }

  render() {
    return (
      <div className="App">
        <TopNavBar />
        <h1>Latest COVID-19 Tweets</h1>
        { <dl className="dictionary">
          {this.state.tweets.map(this.createTwitterCard)}
        </dl> }
      </div>
    );
  }
}

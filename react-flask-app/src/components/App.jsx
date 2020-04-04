import React from "react";
import TopNavBar from "./TopNavBar"
import TweetCard from "./TweetCard"
import '../CSS/App.css';



export default class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = { tweetIds: [] }
    }

    createTwitterCard(tweetId){
        console.log(tweetId)
        return(
            <TweetCard
                key={tweetId}
                tweetId={tweetId}
             />
        );
    }

    componentDidMount() {
        var vm = this;
        fetch('/GetTopPostsState/CO').then(res => res.json()).then(data => {
            vm.setState({
                tweetIds:data
            })
        })
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

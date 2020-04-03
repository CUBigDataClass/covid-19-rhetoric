import React from "react";
import TopNavBar from "./TopNavBar"
import TweetCard from "./TweetCard"
import '../CSS/App.css';

function App() {
    return (
        <div className="App">
            <TopNavBar />
            <TweetCard
                tweetID={"1242905903948496896"}
            />
        </div>
    );
}

export default App;

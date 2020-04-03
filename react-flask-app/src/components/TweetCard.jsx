import React from "react";
import { TwitterTimelineEmbed, TwitterShareButton, TwitterFollowButton, TwitterHashtagButton, TwitterMentionButton, TwitterTweetEmbed, TwitterMomentShare, TwitterDMButton, TwitterVideoEmbed, TwitterOnAirButton } from 'react-twitter-embed';
import '../CSS/App.css';

function TweetCard(props) {
    return (
        <div className="TweetCard">
            <TwitterTweetEmbed tweetId={props.tweetID}/>
        </div>
    );
}

export default TweetCard;

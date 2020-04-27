import React from "react";
import { TwitterTimelineEmbed, TwitterShareButton, TwitterFollowButton, TwitterHashtagButton, TwitterMentionButton, TwitterTweetEmbed, TwitterMomentShare, TwitterDMButton, TwitterVideoEmbed, TwitterOnAirButton } from 'react-twitter-embed';
import '../CSS/App.css';
import Card from 'react-bootstrap/Card'
import 'bootstrap/dist/css/bootstrap.min.css';

function TweetCard(props) {
    console.log(props.tweetId)
    console.log(props.bg)
    return (
        <Card
            bg={props.bg.toLowerCase()}
            text={props.bg.toLowerCase() === 'light' ? 'dark' : 'white'}
            style={{ width: '18rem' }}
        >
            <Card.Header>Tweet</Card.Header>
            <Card.Body>
                <TwitterTweetEmbed tweetId={props.tweetId.toLowerCase()} />
            </Card.Body>
        </Card>
    );
}

export default TweetCard;

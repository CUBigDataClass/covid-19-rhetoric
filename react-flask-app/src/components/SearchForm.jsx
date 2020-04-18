import React from "react";
import TopNavBar from "./TopNavBar"
import TweetCard from "./TweetCard"
import '../CSS/App.css';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

export default class SearchForm extends React.Component {

    constructor(props) {
        super(props);
        this.state = { value: '', tweetIds: [] };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({ value: event.target.value });
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

    handleSubmit(event) {
        var query = this.state.value
        event.preventDefault();
        fetch('/Search/' + query).then(res => res.json()).then(data => {
            this.setState({
                tweetIds: data
            })
        })
    }

    render() {
        return (
            <div className="App">
                <TopNavBar />
                <Form className="searchinput" onSubmit={this.handleSubmit}>
                    <Form.Group controlId="formBasicEmail">
                        <Form.Label className="searchLabel">Enter term to seach Twitter and Reddit</Form.Label>
                        <Form.Control type="input" placeholder="Enter search term" value={this.state.value} onChange={this.handleChange} />
                        <Form.Text className="text-muted">
                        </Form.Text>
                    </Form.Group>

                    <Button variant="primary" type="submit" value="Submit">
                        Submit
            </Button>
                </Form >
                <dl className="dictionary">{this.state.tweetIds.map(this.createTwitterCard)}</dl>
            </div>
        );
    }
}

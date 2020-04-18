import React from "react";
import USMapPage from "./USMapPage";
import Home from "./Home";
import SearchForm from "./SearchForm";

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";

export default class BasicRoute extends React.Component {
    render() {
        return (
            <Router>
                <Switch>
                    <Route path="/USmapTweets">
                        <USMapPage />
                    </Route>
                    <Route path="/Search">
                        <SearchForm />
                    </Route>
                    <Route path="/Home">
                        <Home />
                    </Route>
                    <Route path="/">
                        <Home />
                    </Route>

                </Switch>
            </Router >
        );
    }
}

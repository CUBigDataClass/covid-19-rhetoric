import React from "react";
import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav'
import Navbar from 'react-bootstrap/Navbar'
import NavDropdown from 'react-bootstrap/NavDropdown'
import Form from 'react-bootstrap/Form'
import FormControl from 'react-bootstrap/FormControl'
import 'bootstrap/dist/css/bootstrap.min.css';

function TopNavBar() {
    return (
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand href="/Home">COVID-19 Rhetoric</Navbar.Brand>
            <Nav className="mr-auto">
                <Nav.Link href="/Home">Home</Nav.Link>
                <Nav.Link href="/USmapTweets">Top in US</Nav.Link>
                <Nav.Link href="/Search">Search</Nav.Link>
            </Nav>
        </Navbar>
    );
}

export default TopNavBar;

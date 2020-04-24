import React from 'react';


import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem } from 'reactstrap';

class Navigation extends React.PureComponent {
  render(){
    return (

      <div>
          <Navbar color="light" light expand="md">
            <NavbarBrand href="/">React </NavbarBrand>
            <NavbarToggler />
            <Collapse >
              <Nav className="ml-auto" navbar>


              <NavItem>
                  <NavLink>Home</NavLink>
              </NavItem>
                
                <NavItem>
                  <NavLink>Map </NavLink>
                </NavItem> 
                
                <NavItem>
                  <NavLink href="/register">Search</NavLink>
                </NavItem>
                
            

              
              </Nav>
            </Collapse>
          </Navbar>
        </div>
    );
  }
}

export default Navigation;



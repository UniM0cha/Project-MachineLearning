import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';


const Header = () => {
  return (
    <div>
      <Navbar class="navbar" bg="primary">
        <Container>
          <Navbar.Brand class="navbar-brand" href="/">
            <img src="./img/home3.png" width="65" height="40" alt="/home" />
          </Navbar.Brand>
          <Navbar.Toggle
            class="navbar-toggler"
            aria-controls="basic-navbar-nav"
          />
          <Navbar.Collapse class="navbar-collapse" id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link class="nav-link" href="balju" bs="light">
                수동발주
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </div>
  );
};

export default Header;

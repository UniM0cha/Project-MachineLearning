import React from 'react';
import { Navbar, Nav, Container,Form,FormControl,Button } from 'react-bootstrap';


const Header = () => {

    return (
        <div>
            <Navbar class="navbar" bg="primary">
                <Container>
                    <Navbar.Brand class="navbar-brand" href="/main"><img src="./img/home_heart.png" height="40" alt="/home" /></Navbar.Brand>
                    <Navbar.Toggle class="navbar-toggler" aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse class="navbar-collapse" id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link class="nav-link" href="balju" bs="light" color='white'>수동발주</Nav.Link>
                        </Nav>
                        <Nav className="me-auto">
                            <Nav.Link class="nav-link" href="/" bg="white" >로그아웃</Nav.Link>
                        </Nav>                       
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </div>


    )
}


export default Header;

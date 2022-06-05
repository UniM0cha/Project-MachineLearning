import React from "react";
import { Navbar, Container } from 'react-bootstrap';



const HeaderManage = () => {
    return (
        <div>
        <Navbar  class = "navbar" bg="primary">
            <Container>
                <Navbar.Brand class = "navbar-brand" href="/admin"><img src="./img/home_heart.png"  height = "40"alt = "/home"/></Navbar.Brand>
                <Navbar.Toggle class = "navbar-toggler" aria-controls="basic-navbar-nav" />
            </Container>
        </Navbar>
        </div>
    )
}

export default HeaderManage;
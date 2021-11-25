import React, { useState } from "react";
import styled from "styled-components";
import { Link } from "react-router-dom";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import { IconContext } from "react-icons/lib";
import "../../styles/header.css";
import jt_logo from "../../assets/jt_logo.png";

// Navbar Properties
const Nav = styled.div`
  background: #15171c;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
`;
  
const NavIcon = styled(Link)`
  margin-left: 2rem;
  font-size: 2rem;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const NavIconX = styled(Link)`
  margin-left: 2rem;
  margin-right: 2rem;
  font-size: 2rem;
  height: 80px;
  display: flex;
  justify-content: right;
  align-items: center;
`;
  
// Sidebar properties
const SidebarNav = styled.nav`
  background: #1e90ff;
  width: 230px;
  height: 100vh;
  display: flex;
  justify-content: center;
  position: fixed;
  top: 0;
  left: ${({ sidebar }) => (sidebar ? "0" : "-100%")};
  transition: .3s ease-in-out;
  z-index: 10;
`;
  
const SidebarWrap = styled.div`
  width: 100%;
`;

export const NavBtn = styled.nav`
  display: flex;
  align-items: right;
  margin-right: 24px;
  float: right;
  /* Third Nav */
  /* justify-content: flex-end;
  width: 100vw; */
  @media screen and (max-width: 768px) {
    display: none;
  }
`;
  
export const NavBtnLink = styled(Link)`
  border-radius: 4px;
  background: #808080;
  padding: 10px 22px;
  color: #000000;
  outline: none;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  text-decoration: none;
  /* Second Nav */
  margin-left: 24px;
  &:hover {
    transition: all 0.2s ease-in-out;
    background: #fff;
    color: #808080;
  }
`;
  
const LandingNav = (props) => {
  const [sidebar, setSidebar] = useState(false);
  
  const showSidebar = () => setSidebar(!sidebar);

  const removeToken = () => {
    localStorage.removeItem('token')
    props.setToken(0);
  };

  return (
     
      <>
      <center><img src={jt_logo} class="h1-center" height="120" width="350"/></center>
      {/* <h1 class = "h1-center"> JOB TRACKER </h1> */}
      <IconContext.Provider value={{ color: "#fff" }}>
      <Nav>
        <h1
          style={{
            textAlign: "center",
            marginLeft: "auto",
            marginRight: "auto",
            color: "white"
          }}>
        </h1>

        <NavBtn>
          <NavBtnLink to="/home">Login</NavBtnLink>
        </NavBtn>
        <NavBtn>
          <NavBtnLink to="/signup">Sign Up</NavBtnLink>
        </NavBtn>
      </Nav>
      </IconContext.Provider>
      
      </>
   
  );
  
};

  
export default LandingNav;
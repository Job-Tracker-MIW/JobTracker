import React, { useState } from "react";
import styled from "styled-components";
import { Link } from "react-router-dom";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import { IconContext } from "react-icons/lib";
import "../../styles/header.css";
import "./Landing.css"
import jt_logo from "../../assets/jt_logo.png";
import contacts from "../../assets/contacts.png";
import jobs from "../../assets/jobs.png";
import applications from "../../assets/applications.png";
import skills from "../../assets/skills.png";
import LandingNav from "./LandingNav";

export default class Landing extends React.Component {


    render() {
        return <div>
            <LandingNav></LandingNav>

            <div className="landing-container">
                <div className="white-small">
                    <div className="content">
                        <h1>Welcome to JobTracker!</h1>
                        <p>JobTracker in your one-stop-shop for tracking job applications in Computer Science.</p>
                    </div>
                </div>
                <div className="blue">
                    <div className="content">
                        <center><img src={jobs} class="h1-center"/></center>
                        <center><p>Track job applications with a easy-to-use interface.</p></center>
                    </div>
                </div>
                <div className="white">
                    <div className="content">
                        <center><img src={applications} class="h1-center"/></center>
                        <center><p>Add jobs to your list of applied jobs and track their status.</p></center>
                    </div>
                    
                </div>
                <div className="blue">
                    <div className="content">
                        <center><img src={skills} class="h1-center"/></center>
                        <center><p>Add software your language skills and easily track the demand.</p></center>
                    </div>
                    
                </div>
                <div className="white">
                    <div className="content">
                        <center><img src={contacts} class="h1-center"/></center>
                        <center><p>Track the contacts you've made through jobs you've found and applications submitted.</p></center>
                    </div>
                </div>
                <div className="blue-small">
                </div>
            </div>
        </div>
    }
}
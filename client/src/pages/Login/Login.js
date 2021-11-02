import React, { Component } from "react";
import './Login.css';
import jt_logo from "../../assets/jt_logo.png";

export default class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
            username: "",
            password: "",
            incorrect: false
        }
    }

    handleChangeUsername = (e) => {
        this.setState({ username: e.target.value});
    }

    handleChangePassword = (e) => {
        this.setState({ password: e.target.value});
    }

    submitLogin = (e) => {
        e.preventDefault();
        fetch("/login", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*",
            },
            body: JSON.stringify({"username": this.state.username,
            "password": this.state.password})
        })
        .then(res => res.json())
        .then(data => {
            if (data["response"]) {
                localStorage.setItem('token', data["token"]);
                this.props.setToken(data["token"]);
            } else {
                this.setState({incorrect: true})
            }
        })
    }

    render() {
        return (
        <html>
            <body>
            <center><img src={jt_logo} class="h1-center" height="120" width="350"/></center>
                <div class="box">
                    <div class="form-center">
                        <form>
                        <p className={!this.state.incorrect ? 'hidden incorrect' : 'incorrect'}>Username or password incorrect</p>
                        <h3 class = "h1"> SIGN IN</h3>
                            <div class ="form-group">
                                <label class="right-align-class">Username</label>
                                <input type="text" className="form-control" placeholder="Enter username" onChange={this.handleChangeUsername.bind(this)} />
                            </div>

                            <div class ="form-group">
                                <label class="right-align-class">Password</label>
                                <input type="password" className="form-control" placeholder="Enter password" onChange={this.handleChangePassword.bind(this)} />
                            </div>
                            <div class="form-group">
                                <button className="btn btn-primary" onClick={this.submitLogin}>Submit</button>
                            </div>
                            <p class="form-group">
                                No Login? <a href="#">Sign Up.</a>
                            </p>
                        </form>
                    </div>
                </div>
            </body>
        </html>     
        );
    }
}


import React, { Component } from "react";
import './Signup.css';
import jt_logo from "../../assets/jt_logo.png"
import ReactDOM from 'react-dom';
import { Link, Redirect } from 'react-router-dom';
import { validateNotBlank, validateEmail, validatePasswords} from './SignupValidators';

export default class Signup extends Component {
    constructor(props) {
        super(props);
        this.state = { 
            username: '', 
            email: '', 
            password: '', 
            passwordConfirm: '', 
            signupSuccess: false 
        };
    }

    handleEmailInput = (event) => {
        this.setState({ email: event.target.value });
    }

    handlePasswordInput = (event) => {
        this.setState({ password: event.target.value });
    }

    handleConfirmPasswordInput = (event) => {
        this.setState({ passwordConfirm: event.target.value });
    }

    handleUsernameInput = (event) => {
        this.setState({ username: event.target.value });
    }

    handleSubmit = (event) => {
        event.preventDefault();

        const userdata = this.state
        let checkFields = validateNotBlank(userdata);
        if (checkFields === false) {
            return;
        }
        let email = validateEmail(this.state.email);
        if (email === false) {
            return;
        }
        let passMatch = validatePasswords(userdata['password'], userdata['passwordConfirm'])
        if (passMatch === false) {
            return
        }
        const url = "/usersignup"
        fetch(url, {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
           },
           body: JSON.stringify(userdata)
        })
        .then((response) => response.json())
        .then(data => {
            if (data['response'] === true) {
                this.setState({signupSuccess: true});
            } else {
                const element = <p className="incorrect-text">Username taken</p>;
                ReactDOM.render(element, document.getElementsByClassName('incorrect-creds')[0]);
            }
        })
    }

    render() {
        if (this.state.signupSuccess) {
            return <Redirect to="/"></Redirect>
        }

        return <body>
            <center><img src={jt_logo} class="h1-center" height="120" width="350"/></center>
            <div className="box">
                <div className="form-center">
                    <form className="form">
                        <h1>CREATE ACCOUNT</h1>
                            <div className="form-group">
                                <label class="right-align-class">Username</label>
                                <input
                                className="form-control"
                                placeholder="Enter username"
                                text="Username"
                                ref="user"
                                type="text"
                                defaultValue={this.state.username}
                                value={this.state.username}
                                onChange={this.handleUsernameInput}
                                />
                            </div>
                            <div className="form-group">
                                <label class="right-align-class">Email Address</label>
                                <input
                                    className="form-control"
                                    placeholder="Enter email address"
                                    text="Email Address"
                                    ref="email"
                                    type="email"
                                    defaultValue={this.state.email}
                                    value={this.state.email}
                                    onChange={this.handleEmailInput}
                                />
                            </div>
                            <div className="form-group">
                                <label class="right-align-class">Password</label>
                                <input
                                    className="form-control"
                                    placeholder="Enter password"
                                    text="Password"
                                    type="password"
                                    ref="password"
                                    validator="true"
                                    minCharacters="8"
                                    requireCapitals="1"
                                    requireNumbers="1"
                                    value={this.state.passsword}
                                    onChange={this.handlePasswordInput}
                                />
                            </div>
                            <div className="form-group">
                                <label class="right-align-class">Confirm Password</label>
                                <input
                                    className="form-control"
                                    placeholder="Enter password to confirm"
                                    text="Confirm password"
                                    ref="passwordConfirm"
                                    type="password"
                                    validate={this.isConfirmedPassword}
                                    value={this.state.confirmPassword}
                                    onChange={this.handleConfirmPasswordInput}
                                />
                            </div>
                            <div className="form-group">
                                <button
                                    type="submit"
                                    className="button button-wide"
                                    onClick={this.handleSubmit}>
                                    CREATE ACCOUNT
                                </button>
                            </div>
                            <p className="login-button">Already have an account? <Link to="/">Login.</Link></p>
                            <div className="incorrect-creds"></div>
                        </form>
                    </div>
                </div>
            </body>
    }

}

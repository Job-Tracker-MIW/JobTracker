import React, { Component } from "react";
import './Login.css';

export default class Login extends Component {
    render() {
        return (
        <html>
            <body>
                <div class="box">
                    <div class="form-center">
                        <form>
                        <h3 class = "h1"> SIGN IN</h3>
                            <div class ="form-group">
                                <label class="right-align-class">Email address</label>
                                <input type="email" className="form-control" placeholder="Enter email" />
                            </div>

                            <div class ="form-group">
                                <label class="right-align-class">Password</label>
                                <input type="password" className="form-control" placeholder="Enter password" />
                            </div>
                            <div class="form-group">
                                <button type="submit" className="btn btn-primary">Submit</button>
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


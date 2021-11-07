import React, { } from 'react';
import '../../styles/tableCSS.css';
import './contacts.css'

export default class ContactAdd extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isAdding: false,
            contact: this.props.contact, // contact = name
            company: this.props.company,       // company = companyid
            email: this.props.email,       // email = email
            phone: this.props.phone,       // email = email
            jobCount: this.props.jobCount       // email = email
        }
    }

    handleChangeContact = (e) => {
        this.setState({ contact: e.target.value});
    }

   
    handleChangeEmail = (e) => {
        this.setState({ email: e.target.value});
    }

    handleChangePhone = (e) => {
        this.setState({ phone: e.target.value});
    }

    handleChangeCo = (e) => {
        this.setState({ company: e.target.value});
    }
 

    setIsAdding = () => {
        this.setState({isAdding: true});
    };

    submitRow = () => {
        fetch("/contacts", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },
            body: JSON.stringify({"name": this.state.contact,
            "email": this.state.email,
            "phone": this.state.phone,
            "company": this.state.company,
            "jobCount": this.state.jobCount

	    })
        })
        .then(res => {
            console.log(res);
            this.setState({isAdding: false});
            this.props.onRefresh()});
    }

    cancelAdding = () => {
        this.setState({isAdding: false});
    }
  
    render() {
        return <tr>
            <button onClick={this.setIsAdding} className={this.state.isAdding?  'hidden' : undefined}>Add</button>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeContact.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeEmail.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangePhone.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeCo.bind(this)} /></td>
            <td className={!this.state.isAdding?  'hidden' : undefined}></td>
            <button onClick={this.submitRow} className={!this.state.isAdding ? 'hidden' : undefined}>Submit</button>
            <button onClick={this.cancelAdding} className={!this.state.isAdding ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}

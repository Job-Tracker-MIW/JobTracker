import React, { } from 'react';
import '../../styles/tableCSS.css';
import './contacts.css'

export default class ContactRow extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isEditing: false,
            contact: this.props.contact, // contact = name
	    email: this.props.email,       // email = email
	    phone: this.props.phone,       // email = email
	    company: this.props.company,       // company = company
	    jobCount: this.props.jobCount       // jobCount = jobCount
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



    setIsEditing = () => {
        this.setState({isEditing: true});
    };

    deleteRow = () => {
        fetch("/contacts/" + this.props.contactid, {
            method: 'DELETE',
	    headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },

        })
        .then(res => {
            console.log(res);
            this.props.onRefresh()})
    }

    updateRow = () => {
        fetch("/contacts/" + this.props.contactid, {
            method: 'PUT',
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
            this.props.onRefresh()})
    }

    cancelEditing = () => {
        this.setState({isEditing: false});
    }
  
    render() {
        return <tr>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.contact} onChange={this.handleChangeContact.bind(this)} /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.email} onChange={this.handleChangeEmail.bind(this)} /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.phone} onChange={this.handleChangePhone.bind(this)} /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.company} onChange={this.handleChangeCo.bind(this)} /></td>
            <td>{this.props.jobCount}</td>
            <button onClick={this.deleteRow} className={!this.state.isEditing ?  'hidden' : undefined}>Delete</button>
            <button onClick={this.updateRow} className={!this.state.isEditing ? 'hidden' : undefined}>Update</button>
            <button onClick={this.cancelEditing} className={!this.state.isEditing ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}

import React, { } from 'react';
import '../../styles/tableCSS.css';
import './companies.css'

export default class CompanyRow extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isEditing: false,
            company: this.props.company,
            contacts: this.props.contacts,
        }
    }

    handleChangeCompany = (e) => {
        this.setState({ company: e.target.value});
    }

    handleChangePro = (e) => {
        this.setState({ contacts: e.target.value});
    }

    setIsEditing = () => {
        this.setState({isEditing: true});
    };

    deleteRow = () => {
        fetch("/companies/" + this.props.companyid, {
            method: 'DELETE'
        })
        .then(res => {
            console.log(res);
            this.props.onRefresh()})
    }

    updateRow = () => {
        fetch("/companies/" + this.props.companyid, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"name": this.state.company,
            "contacts": this.state.contacts})
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
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.company} onChange={this.handleChangeCompany.bind(this)} /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.pro} onChange={this.handleChangePro.bind(this)} /></td>
            <td>{this.props.jobMatch}</td>
            <button onClick={this.deleteRow} className={this.state.isEditing?  'hidden' : undefined}>Delete</button>
            <button onClick={this.updateRow} className={!this.state.isEditing ? 'hidden' : undefined}>Update</button>
            <button onClick={this.cancelEditing} className={!this.state.isEditing ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}
import React, { } from 'react';
import '../../styles/tableCSS.css';
import './companies.css'

export default class CompanyRow extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isEditing: false,
            company: this.props.company,
            title: this.props.title,
            name: this.props.name,
            jobid: this.props.jobid,
            companyid: this.props.companyid
        }
    }

    handleChangeCompany = (e) => {
        this.setState({ company: e.target.value});
    }

    handleChangeTitle = (e) => {
        this.setState({ title: e.target.value});
    }

    handleChangeName = (e) => {
        this.setState({ name: e.target.value});
    }

    handleChangeJobID = (e) => {
        this.setState({ jobid: e.target.value});
    }

    handleChangeCompanyID = (e) => {
        this.setState({ companyid: e.target.value});
    }

    setIsEditing = () => {
        this.setState({isEditing: true});
    };

    deleteRow = () => {
        // fetch("/companies/" + this.props.jobid, {
        fetch("/companies", {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
        },
        body: JSON.stringify({"jobid": this.state.jobid,
        "companyid": this.state.companyid 
            })
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
            body: JSON.stringify({"company": this.state.company, 
            "title": this.state.title,
            "name": this.state.name})
        })
        .then(res => {
            console.log(res);
            this.props.onRefresh()})
    }

    // Need to finish this when Mat's portion is done
    applyForJob = () => {
        fetch("/appjobs", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },
            body: JSON.stringify({"title": this.state.title,
            "company": this.state.company,
            "jobid": this.state.jobid
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
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.company} onChange={this.handleChangeCompany.bind(this)} /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.title} onChange={this.handleChangeTitle.bind(this)} /></td>
            <td>{this.props.name}</td>
            <button onClick={this.applyForJob} className={this.state.isEditing?  'hidden' : undefined}>Applied</button>
            <button onClick={this.deleteRow} className={this.state.isEditing?  'hidden' : undefined}>Delete</button>
            <button onClick={this.updateRow} className={!this.state.isEditing ? 'hidden' : undefined}>Update</button>
            <button onClick={this.cancelEditing} className={!this.state.isEditing ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }

}
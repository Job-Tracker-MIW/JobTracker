import React, { } from 'react';
import '../../styles/tableCSS.css';
import './AppliedJobs.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

export default class AppliedJobsAdd extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isAdding: false,
            title: this.props.title,
            name: this.props.name,
            company: this.props.company,
            status: this.props.status,
            appdt: this.props.appdt,
            companies: this.props.companies
        }
    }

    options = [
        'Applied', 'Online Assessment', 'Interview Scheduled', 
        'Rejected', 'Offer Received', 'Accepted'
      ];

    handleChangeTitle = (e) => {
        this.setState({ title: e.target.value});
    }

    handleChangeCompany = (e) => {
        this.setState({ company: e});
    }

    handleChangeName = (e) => {
        this.setState({ name: e.target.value});
    }

    handleChangeAppdt = (e) => {
        this.setState({ appdt: e.target.value});
    }

    handleChangeStatus = (e) => {
        this.setState({ status: e.target.value});
    }

    setIsAdding = () => {
        this.setState({isAdding: true});
    };

    handleChangeStatus = (option) => {
        this.setState({status: option})
    };

    submitRow = () => {
        fetch("/appjobs", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },
            body: JSON.stringify({"title": this.state.title,
            "company": this.state.company,
            "status": this.state.status,
            "appdt": this.state.appdt,
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
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeTitle.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><Dropdown options={this.props.companies} onChange={this.handleChangeCompany} value={this.props.company} placeholder="Select a company" /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeName.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><DatePicker selected={this.state.appdt} onChange={this.handleChangeAppdt} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><Dropdown options={this.options} onChange={this.handleChangeStatus} value={this.props.status} placeholder="Select a status" /></td>
            <td className={!this.state.isAdding?  'hidden' : undefined}></td>
            <button onClick={this.submitRow} className={!this.state.isAdding ? 'hidden' : undefined}>Submit</button>
            <button onClick={this.cancelAdding} className={!this.state.isAdding ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}

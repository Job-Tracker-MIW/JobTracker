import React, { } from 'react';
import '../../styles/tableCSS.css';
import './AppliedJobs.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

export default class AppliedJobsRow extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isEditing: false,
            title: this.props.title,
            name: this.props.name,
            company: this.props.company,
            status: this.props.status,
            appdt: Date.parse(this.props.appdt) || new Date(),
            companies: this.props.companies
        }

        console.log(typeof this.state.appdt + " " + this.state.appdt)
    }

    companyOptions = [];

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
        this.setState({ appdt: e});
    }

    handleChangeStatus = (e) => {
        this.setState({ status: e.target.value});
    }

    setIsEditing = () => {
        this.setState({isEditing: true});
    };

    handleChangeStatus = (option) => {
        this.setState({status: option})
    };


    deleteRow = () => {
        fetch("/appjobs/" + this.props.appid, {
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
        fetch("/appjobs/" + this.props.appid, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },
              body: JSON.stringify({"title": this.state.title,
		                  "company": this.state.company,
		                  "name": this.state.name | "",
		                  "appdt": this.state.appdt,
		                  "status": this.state.status,
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
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.title} onChange={this.handleChangeTitle.bind(this)} /></td>
            <td onClick={this.setIsEditing}><Dropdown options={this.props.companies} onChange={this.handleChangeCompany} value={this.props.company} placeholder="Select a company" /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.name} onChange={this.handleChangeName.bind(this)} /></td>
            <td onClick={this.setIsEditing}><DatePicker selected={this.state.appdt} onChange={this.handleChangeAppdt} /></td>
            <td onClick={this.setIsEditing}><Dropdown options={this.options} onChange={this.handleChangeStatus} value={this.props.status} placeholder="Select a status" /></td>
            <button onClick={this.deleteRow} className={!this.state.isEditing?  'hidden' : undefined}>Delete</button>
            <button onClick={this.updateRow} className={!this.state.isEditing ? 'hidden' : undefined}>Update</button>
            <button onClick={this.cancelEditing} className={!this.state.isEditing ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}

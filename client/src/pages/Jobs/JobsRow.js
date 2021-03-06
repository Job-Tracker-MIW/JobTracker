import React, { } from 'react';
import '../../styles/tableCSS.css';
import './jobs.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';

export default class JobsRow extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isEditing: false,
            company: this.props.company,
            title: this.props.title,
            userDefName: this.props.userDefName,
            name: this.props.name,
            jobid: this.props.jobid,
            companyid: this.props.companyid,
            skill: this.props.skill,
            unique_company_id: this.props.unique_company_id
        }
    }

    options = [
        'Assembly', 'C', 'C++', 'C#', 'Java', 'Javascript', 'Python', 'HTML/CSS', 'Swift', 'R', 
        'Go', 'Scala', 'PHP', 'SQL', 'Ruby'
    ]

    handleChangeCompany = (e) => {
        this.setState({ company: e.target.value});
    }

    handleChangeSkill = (e) => {
        this.setState({ skill: e.value});
    }

    handleChangeTitle = (e) => {
        this.setState({ title: e.target.value});
    }

    handleChangeUserDefName = (e) => {
        this.setState({ userDefName: e.target.value});
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
        "companyid": this.state.companyid, 
        "userDefName": this.state.userDefName
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
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },
            body: JSON.stringify({"company": this.state.company, 
            "title": this.state.title,
            "userDefName": this.state.userDefName,
            "name": this.state.name,
            "skill": this.state.skill,
            "companyid": this.state.companyid,
            "jobid": this.state.jobid,
            "unique_company_id": this.state.unique_company_id})
        })
        .then(res => {
            console.log(res);
            // this.setState({isEditing: false});
            this.props.onRefresh()});
            this.setState({isEditing: false});
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
		    "userDefName": this.state.userDefName,
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
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.userDefName} onChange={this.handleChangeUserDefName.bind(this)} /></td>
            <td>{this.props.name}</td>
            <td onClick={this.setIsEditing}><Dropdown options={this.options} onChange={this.handleChangeSkill} value={this.props.skill} placeholder="Select a language"/></td>
            <button onClick={this.applyForJob} className={this.state.isEditing?  'hidden' : undefined}>Applied</button>
            <button onClick={this.deleteRow} className={this.state.isEditing?  'hidden' : undefined}>Delete</button>
            <button onClick={this.updateRow} className={!this.state.isEditing ? 'hidden' : undefined}>Update</button>
            <button onClick={this.cancelEditing} className={!this.state.isEditing ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }

}

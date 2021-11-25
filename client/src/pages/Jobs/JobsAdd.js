import React, { } from 'react';
import '../../styles/tableCSS.css';
import './jobs.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';

export default class JobsAdd extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isAdding: false,
            company: this.props.company,
            title: this.props.title,
            userDefName: this.props.userDefName,
            name: this.props.name,
            jobid: this.props.jobid,
            companyid: this.props.companyid,
            skill: this.props.skill
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

    setIsAdding = () => {
        this.setState({isAdding: true});
    };
    
    addCompany = () => {
        fetch("/companies", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },
            body: JSON.stringify({"title": this.state.title,
		    "userDefName": this.state.userDefName,
            "company": this.state.company, 
            "companyid": this.state.companyid,
            "skill": this.state.skill})
        })
        .then(res => {
            console.log(res);
            this.props.onRefresh()});
            this.setState({isAdding: false});
            
    }

    cancelAdding = () => {
        this.setState({isAdding: false});
    }

    render() {
        return <tr>
            <button onClick={this.setIsAdding} className={this.state.isAdding ? 'hidden' : undefined}>Add</button>
            <td onClick={this.setIsEditing} className={!this.state.isAdding ? 'hidden' : undefined}><input type="text" placeholder="Company Name" onChange={this.handleChangeCompany.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding ? 'hidden' : undefined}><input type="text" placeholder="Job Title" onChange={this.handleChangeTitle.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding ? 'hidden' : undefined}><input type="text" placeholder="User defined name" onChange={this.handleChangeUserDefName.bind(this)} /></td>
            <td className={!this.state.isAdding ? 'hidden' : undefined}></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding ? 'hidden' : undefined}><Dropdown options={this.options} onChange={this.handleChangeSkill} value={this.props.skill} placeholder="Select a language"/></td>
            <button onClick={this.addCompany} className={!this.state.isAdding ? 'hidden' : undefined}>Submit</button>
            <button onClick={this.cancelAdding} className={!this.state.isAdding ? 'hidden' : undefined}>Cancel</button>
        </tr>
   
    }
}





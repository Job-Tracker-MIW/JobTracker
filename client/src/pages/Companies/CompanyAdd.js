import React, { } from 'react';
import '../../styles/tableCSS.css';
import './companies.css'

export default class CompanyAdd extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isAdding: false,
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
            "company": this.state.company, 
            "companyid": this.state.companyid})

        })
        .then(res => {
            console.log(res);
            this.setState({isAdding: false});
            this.props.onRefresh()})
    }

    cancelAdding = () => {
        this.setState({isAdding: false});
    }

    render() {
        return <tr>
            <button onClick={this.setIsAdding} className={this.state.isAdding ? 'hidden' : undefined}>Add</button>
            <td onClick={this.setIsEditing} className={!this.state.isAdding ? 'hidden' : undefined}><input type="text" placeholder="Company Name" onChange={this.handleChangeCompany.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding ? 'hidden' : undefined}><input type="text" placeholder="Job Title" onChange={this.handleChangeTitle.bind(this)} /></td>
            <td className={!this.state.isAdding ? 'hidden' : undefined}></td>
            <button onClick={this.addCompany} className={!this.state.isAdding ? 'hidden' : undefined}>Submit</button>
            <button onClick={this.cancelAdding} className={!this.state.isAdding ? 'hidden' : undefined}>Cancel</button>
        </tr>
   
    }
}





import React, { } from 'react';
import '../../styles/tableCSS.css';
import './AppliedJobs.css'

export default class AppliedJobsAdd extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isAdding: false,
            title: this.props.title,
            company: this.props.company,
            appdt: this.props.appdt,
        }
    }

    handleChangeTitle = (e) => {
        this.setState({ title: e.target.value});
    }

    handleChangeCompany = (e) => {
        this.setState({ company: e.target.value});
    }

    handleChangeAppdt = (e) => {
        this.setState({ appdt: e.target.value});
    }

    setIsAdding = () => {
        this.setState({isAdding: true});
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
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeCompany.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeAppdt.bind(this)} /></td>
            <td className={!this.state.isAdding?  'hidden' : undefined}></td>
            <button onClick={this.submitRow} className={!this.state.isAdding ? 'hidden' : undefined}>Submit</button>
            <button onClick={this.cancelAdding} className={!this.state.isAdding ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}

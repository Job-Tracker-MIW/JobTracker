import React, { } from 'react';
import '../../styles/tableCSS.css';
import './AppliedJobs.css'

export default class AppliedJobsRow extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isEditing: false,
            title: this.props.title,
            name: this.props.name,
            company: this.props.company,
            appdt: this.props.appdt,
            status: this.props.status,
        }
    }

    handleChangeTitle = (e) => {
        this.setState({ title: e.target.value});
    }

    handleChangeCompany = (e) => {
        this.setState({ company: e.target.value});
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


    setIsEditing = () => {
        this.setState({isEditing: true});
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
		                  "name": this.state.name,
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
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.company} onChange={this.handleChangeCompany.bind(this)} /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.name} onChange={this.handleChangeName.bind(this)} /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.appdt} onChange={this.handleChangeAppdt.bind(this)} /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.status} onChange={this.handleChangeStatus.bind(this)} /></td>
            <button onClick={this.deleteRow} className={!this.state.isEditing?  'hidden' : undefined}>Delete</button>
            <button onClick={this.updateRow} className={!this.state.isEditing ? 'hidden' : undefined}>Update</button>
            <button onClick={this.cancelEditing} className={!this.state.isEditing ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}

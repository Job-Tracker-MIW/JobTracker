import React, { } from 'react';
import '../../styles/tableCSS.css';
import './skillLinks.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';

export default class SkillLinksRow extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isEditing: false,
            skill: this.props.skill,
            reslabel: this.props.reslabel,
            reslink: this.props.reslink,
            skillList: this.props.skillList
           	
        }

    }

    options = [] 

    //options = [] 

    handleChangeSkill = (e) => {
        this.setState({ skill: e.value});
    }

    handleChangeResLabel = (e) => {
        this.setState({ reslabel: e.target.value});
    }

    handleChangeResLink = (e) => {
        this.setState({ reslink: e.target.value});
    }

    setIsEditing = () => {
        this.setState({isEditing: true});
    };

    deleteRow = () => {
        fetch("/skillLinks/" + this.props.linkid, {
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
        fetch("/skillLinks/" + this.props.linkid, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },
            body: JSON.stringify({"skill": this.state.skill,
            "reslabel": this.state.reslabel,
            "reslink": this.state.reslink})
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
            <td onClick={this.setIsEditing}><Dropdown options={this.props.skillList} onChange={this.handleChangeSkill} value={this.props.skill} placeholder="Select a language"/></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.reslabel} onChange={this.handleChangeResLabel.bind(this)} /></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.reslink} onChange={this.handleChangeResLink.bind(this)} /></td>
            <button onClick={this.deleteRow}>Delete</button>
            <button onClick={this.updateRow} className={!this.state.isEditing ? 'hidden' : undefined}>Update</button>
            <button onClick={this.cancelEditing} className={!this.state.isEditing ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }

}

import React, { } from 'react';
import '../../styles/tableCSS.css';
import './skills.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';

export default class SkillRow extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isEditing: false,
            skill: this.props.skill,
            pro: this.props.pro,
        }
    }

    options = [
        'Assembly', 'C', 'C++', 'C#', 'Java', 'Javascript', 'Python', 'HTML/CSS', 'Swift', 'R', 
        'Go', 'Scala', 'PHP', 'SQL', 'Ruby'
    ]

    handleChangeSkill = (e) => {
        this.setState({ skill: e.value});
    }

    handleChangePro = (e) => {
        this.setState({ pro: e.target.value});
    }

    setIsEditing = () => {
        this.setState({isEditing: true});
    };

    deleteRow = () => {
        fetch("/skills/" + this.props.skillid, {
            method: 'DELETE',
            headers: {'token': localStorage.getItem('token')}
        })
        .then(res => {
            console.log(res);
            this.props.onRefresh()})
    }

    updateRow = () => {
        fetch("/skills/" + this.props.skillid, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },
            body: JSON.stringify({"name": this.state.skill,
            "proficiency": this.state.pro})
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
            <td onClick={this.setIsEditing}><Dropdown options={this.options} onChange={this.handleChangeSkill} value={this.props.skill} placeholder="Select a language"/></td>
            <td onClick={this.setIsEditing}><input type="text" defaultValue={this.props.pro} onChange={this.handleChangePro.bind(this)} /></td>
            <td>{this.props.jobMatch}</td>
            <button onClick={this.deleteRow}>Delete</button>
            <button onClick={this.updateRow} className={!this.state.isEditing ? 'hidden' : undefined}>Update</button>
            <button onClick={this.cancelEditing} className={!this.state.isEditing ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}

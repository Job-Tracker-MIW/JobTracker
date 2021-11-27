import React, { } from 'react';
import '../../styles/tableCSS.css';
import './skillLinks.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';

export default class SkillLinksAdd extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isAdding: false,
            skill: this.props.skill,
            reslabel: this.props.reslabel,
            reslink: this.props.reslink,
            skillList: this.props.skillList		
	}

    }



    handleChangeSkill = (e) => {
        this.setState({ skill: e});
    }

    handleChangeResLabel = (e) => {
        this.setState({ reslabel: e.target.value});
    }

    handleChangeResLink = (e) => {
        this.setState({ reslink: e.target.value});
    }
	//options = ['C++', 'Javascript', 'Python']



    setIsAdding = () => {
        this.setState({isAdding: true});
    };

    submitRow = () => {
        fetch("/skillLinks", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'token': localStorage.getItem('token')
            },
            body: JSON.stringify({"skill": this.state.skill,
            "reslabel": this.state.reslabel,
            "reslink": this.state.reslink
	    })
        })
        .then(res => {
            this.setState({isAdding: false});
            this.props.onRefresh()});
    }

    cancelAdding = () => {
        this.setState({isAdding: false});
    }
  
    render() {
        return <tr>
            <button onClick={this.setIsAdding} className={this.state.isAdding?  'hidden' : undefined}>Add</button>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><Dropdown options={this.props.skillList} onChange={this.handleChangeSkill} value={this.props.skill} placeholder="Select a Skill"/></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeResLabel.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeResLink.bind(this)} /></td>
            <td className={!this.state.isAdding?  'hidden' : undefined}></td>
            <button onClick={this.submitRow} className={!this.state.isAdding ? 'hidden' : undefined}>Submit</button>
            <button onClick={this.cancelAdding} className={!this.state.isAdding ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}

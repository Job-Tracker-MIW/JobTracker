import React, { } from 'react';
import '../../styles/tableCSS.css';
import './skills.css'

export default class SkillAdd extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            isAdding: false,
            skill: this.props.skill,
            pro: this.props.pro,
        }
    }

    handleChangeSkill = (e) => {
        this.setState({ skill: e.target.value});
    }

    handleChangePro = (e) => {
        this.setState({ pro: e.target.value});
    }

    setIsAdding = () => {
        this.setState({isAdding: true});
    };

    submitRow = () => {
        fetch("/skills", {
            method: 'POST',
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
            this.setState({isAdding: false});
            this.props.onRefresh()});
    }

    cancelAdding = () => {
        this.setState({isAdding: false});
    }
  
    render() {
        return <tr>
            <button onClick={this.setIsAdding} className={this.state.isAdding?  'hidden' : undefined}>Add</button>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangeSkill.bind(this)} /></td>
            <td onClick={this.setIsEditing} className={!this.state.isAdding?  'hidden' : undefined}><input type="text" onChange={this.handleChangePro.bind(this)} /></td>
            <td className={!this.state.isAdding?  'hidden' : undefined}></td>
            <button onClick={this.submitRow} className={!this.state.isAdding ? 'hidden' : undefined}>Submit</button>
            <button onClick={this.cancelAdding} className={!this.state.isAdding ? 'hidden' : undefined}>Cancel</button>
        </tr>
    }
}
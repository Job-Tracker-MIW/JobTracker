import React, { } from 'react';
import '../../styles/tableCSS.css';
import './skills.css'

export default class SkillRow extends React.Component {
  
    render() {
        return <tr>
            <td>{this.props.skill}</td>
            <td>{this.props.pro}</td>
            <td>{this.props.jobMatch}</td>
        </tr>
    }
}
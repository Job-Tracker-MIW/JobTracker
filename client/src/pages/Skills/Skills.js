import React, {useMemo, useState, useEffect, Component } from 'react';
import { makeRenderer, useTable } from "react-table";
import '../../styles/tableCSS.css';
import SkillRow from './SkillRow';
import './skills.css'

export default class Skills extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      error: null,
      skills: []
    }
    this.getSkills();
  }

  getSkills() {
    fetch("/skills")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            skills: result.tableData
          });
        },
        (error) => {
          this.setState({
            error
          });
        }
      )
  }

  render() {
    return <div className='table-container'>
      <div className='title'>
          <h1 className="h1">Skills</h1>
      </div>
      <table class="center">
        <thead>
          <tr>
            <th>Skill</th>
            <th>Proficiency (1-10)</th>
            <th>Job Matches</th>
          </tr>
        </thead>
        <tbody>
        {this.state.skills.map(element =>
                    <SkillRow key={element.skill} {...element}/>
            )}
        </tbody>
      </table>
    </div>

  }
}

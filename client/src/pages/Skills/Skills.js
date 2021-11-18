import React, { } from 'react';
import '../../styles/tableCSS.css';
import SkillAdd from './SkillAdd';
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

  getSkills = () => {
    const options = {
      method: 'GET',
      headers: {'token': localStorage.getItem('token')}
    }
    fetch("/skills", options)
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
          <h1 className="h1">Language Skills</h1>
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
                    <SkillRow onRefresh={this.getSkills} key={element.skillid} {...element}/>
            )}
            <SkillAdd onRefresh={this.getSkills}></SkillAdd>
        </tbody>
      </table>
    </div>

  }
}

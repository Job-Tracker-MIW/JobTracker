import React, { } from 'react';
import '../../styles/tableCSS.css';
import SkillLinksAdd from './SkillLinksAdd';
import SkillLinksRow from './SkillLinksRow';
import './skillLinks.css';

export default class SkillLinks extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      error: null,
      skills: [],
    }
    this.getSkillLinks();
  }

  getSkillLinks = () => {
    const options = {
      method: 'GET',
      headers: {'token': localStorage.getItem('token')}
    }
    fetch("/skillLinks", options)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            skills: result.tableData,
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
          <h1 className="h1">Get Skillz</h1>
      </div>
      <table class="center">
        <thead>
          <tr>
            <th>Skill</th>
            <th>Resource</th>
            <th>Link</th>
          </tr>
        </thead>
        <tbody>
        {this.state.skills.map(element =>
                    <SkillLinksRow onRefresh={this.getSkillLinks} key={element.skillid} {...element}/>
            )}
                    <SkillLinksAdd onRefresh={this.getSkillLinks} skillList={this.state.skills.length > 0 ? this.state.skills[0].skillList : []}></SkillLinksAdd>
			 
        </tbody>
      </table>
    </div>


  }
}

import React, { } from 'react';
import '../../styles/tableCSS.css';
import JobsAdd from './JobsAdd';
import JobsRow from './JobsRow';
import './jobs.css'

// check companies class
export default class Jobs extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      error: null,
      companies: []
    }
    this.getCompanies();
  }

  getCompanies = () => {
    const options = {
      method: 'GET',
      headers: {'token': localStorage.getItem('token')}
    }
    fetch("/companies", options)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            companies: result.tableData
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
          <h1 className="h1">Jobs</h1>
      </div>

      <table class="center">
        <thead>
          <tr>
            <th>Company</th>
            <th>Job Title</th>
            <th>Contact</th>
            <th>Language Skill</th>
          </tr>
        </thead>
        <tbody>
        {this.state.companies.map(element =>
                    <JobsRow onRefresh={this.getCompanies} key={element.companyid} {...element}/>
            )}
            <JobsAdd onRefresh={this.getCompanies} ></JobsAdd>
        </tbody>
      </table>
    </div>
  }
}
